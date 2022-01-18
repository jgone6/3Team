from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Comment.models import Comment
from Comment.form import CommentForm

@login_required(login_url='/login/')
def like(request, bid):
    post = Comment.objects.get( Q(id=bid) )
    user = request.user
    if post.like.filter(id=user.id).exists():
        post.like.remove(user)          # 게시글 좋아요 push
        message = 'del'

    else:                               # 게시글에 좋아요 아직 push 안함
        post.like.add(user)
        message = 'add'

    return JsonResponse({'message' : message, 'like_cnt' : post.like.count()})


def home(request):

    return render(request, 'index.html')

# 로그인을 해야 함수를 실행 시킬 수 있음
@login_required(login_url='/login/')
def register(request):
    if request.method == 'GET':
        commentForm = CommentForm()

        return render(request, 'comment/register.html', {'commentForm' : commentForm})

    elif request.method == 'POST':
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.writer = request.user

            comment.save()
            return redirect('/register/')


def posts(request):
    posts = Comment.objects.all()

    return render(request, 'comment/list.html', {'posts' : posts})

def post(request, bid):
    post = Comment.objects.get( Q(id=bid) )

    return render(request, 'comment/post.html', {'post' : post})

@login_required(login_url='/login/')
def delete(request, bid):
    delete = Comment.objects.get( Q(id=bid))

    if request.user != delete.writer:
        return redirect('/list/')

    delete.delete()

    return redirect('/list/')

@login_required(login_url='/login/')
def update(request, bid):
    update = Comment.objects.get( Q(id=bid) )

    if request.user != update.writer:
        return redirect('/list/')

    if request.method == 'GET':
        commentForm = CommentForm(instance=update)

        return render(request, 'comment/update.html', {'commentForm' : commentForm})

    elif request.method == 'POST':
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            update.title = commentForm.cleaned_data['title']
            update.contents = commentForm.cleaned_data['contents']

            update.save()

            return redirect('/list/')
