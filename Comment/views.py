from django.db.models import Q

from Video.models import Video
from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, redirect


def comment_list(request):
    comment_list = Comment.objects.all()

    return render(request, 'comment/list.html', {'comment_list': comment_list})

def write2(request):
    if request.method == "GET":
        commentform = CommentForm()  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'comment/write.html',
                      {'form': commentform})
    elif request.method == 'POST':
        commentform = CommentForm(request.POST, request.FILES)

        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.save()
            return redirect('/comment/list')
        else:
            commentform = CommentForm()
            return render(request, 'Comment/write.html', {'form': commentform})




def write(request,bid):
    if request.method == "GET":
        commentForm = CommentForm()
        return render(request, 'comment/write.html', {'commentForm': commentForm})

    elif request.method == "POST":
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():

            comment = commentForm.save(commit=False)
            comment.member_id = request.user
            comment.video_id = Video.objects.get(Q(id=bid))
            comment.save()
            return redirect('/Video/read/'+ str(bid))


def comment_content(request, bid):
    comment_content = Comment.objects.get(Q(id=bid))
    return render(request, 'comment/comment.html', {'content': comment_content})


def comment_delete(request, bid):
    delete = Comment.objects.get(Q(id=bid))
    delete.delete()
    return redirect('/comment/list')


def comment_update(request, bid):
    comment_update = Comment.objects.get(Q(id=bid))
    if request.method == "GET":
        commentForm = CommentForm(instance=comment_update)
        return render(request, 'comment/update.html', {'commentForm': commentForm})

    elif request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment_update.contents = commentForm.cleaned_data['contents']
            comment_update.save()
            return redirect('/comment/list')




# Create your views here.
