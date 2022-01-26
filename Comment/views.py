from .forms import CommentForm
from .models import Comment


def comment_list(request):
    comment_list = Comment.objects.all()
    print('***')
    print(comment_list)
    return render(request, 'comment/list.html', {'comment_list': comment_list})


def write(request):
    if request.method == "GET":
        commentForm = CommentForm()
        return render(request, 'comment/write.html', {'commentForm': commentForm})

    elif request.method == "POST":
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            print('**')
            comment = commentForm.save(commit=False)
            comment.save()
            return redirect('/comment/list')


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


from django.shortcuts import render

# Create your views here.
