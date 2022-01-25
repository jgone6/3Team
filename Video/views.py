from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from Video.forms import VideoForm
from django.views.decorators.http import require_POST
import requests
import json
from Video.models import Video

from .forms import VideoForm

def test2(request):

    return render(request, 'Video/test2.html')

def getTag(request, tags):
    print(tags)
    posts = Video.objects.all().filter(tag=tags)

    json = []
    for post in posts:
        json_post = {'id' : post.id, 'title': post.title, 'tag':post.tag, 'file':post.file.name, 'file2':post.file2.name}
        json.append(json_post)

    return JsonResponse({'message':json})

@login_required(login_url='/users/login')
def upload(request):
    if request.method == "GET":
        videoform = VideoForm()  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'video/upload.html',
                      {'form': videoform})
    elif request.method == 'POST':
        videoform = VideoForm(request.POST, request.FILES)

        if videoform.is_valid():
            video = videoform.save(commit=False)
            video.writer = request.user
            video.save()
            return redirect('/Video/mylist')
        else:
            videoform = VideoForm()
            return render(request, 'Video/upload.html', {'form': videoform})






def ss(request):
    posts = Video.objects.all()
    return render(request, 'video/list.html', {'posts': posts})

def posts(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list.html',
                  {'posts': posts})

def myposts(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/mylist.html',
                  {'posts': posts})

def read(request, bid) :
    post = Video.objects.get( Q(id=bid))
    posts = Video.objects.all()
    #posts = Board.objects.all()
    return render(request, 'Video/read.html',{'read' : post, 'posts':posts })
    # #board/read.html페이지를 보여주고 Board.objects.get( Q(id=bid))의 값
    # 을 'read'로 저장한다.

def readmine(request, bid) :
    post = Video.objects.get( Q(id=bid))
    #posts = Board.objects.all()
    return render(request, 'Video/readmine.html',{'read' : post})
    # #board/read.html페이지를 보여주고 Board.objects.get( Q(id=bid))의 값
    # 을 'read'로 저장한다.

# def list_tag(request, tag) :
#     post = Video.objects.get(Q(tag=tag))
#     return render(request, 'Video/list_music.html',{'list' : post})

def list_music(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_music.html',
                  {'posts': posts})
def list_var(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_var.html',
                  {'posts': posts})
def list_geo(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_geo.html',
                  {'posts': posts})
def list_edu(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list_edu.html',
                  {'posts': posts})




@login_required(login_url='/users/login')
def delete(request, bid) :
    post = Video.objects.get(Q(id = bid))
    if request.user != post.writer:
        return render(request,'Video/list.html')
    post.delete()
    return redirect('/Video/list')



# @login_required(login_url='/users/login')
# def update(request, bid) :
#     post = Video.objects.get(Q(id=bid))  #게시글 하나를 가져오는것
#     if request.method == "GET" :
#         videoForm = VideoForm()
#         #특정 조건 id에 해당하는 값을 저장한다.
#         return render(request,'Video/update.html',{'videoForm' : videoForm})
#     elif request.method == "POST" :
#         videoForm = VideoForm(request.POST, request.FILES)
#         print(videoForm.cleaned_data['title'])
#         if videoForm.is_valid():   #boardForm안에 값이 유효한다
#             post.title = videoForm.cleaned_data['title']
#             post.tag = videoForm.cleaned_data['tag']
#             post.file = videoForm.cleaned_data['file']
#             post.file2 = videoForm.cleaned_data['file2']
#             post.writer = request.user
#             post.save()
#             print("1")
#             return redirect('/Video/list')
#
#             # return render(request, 'Video/list.html',)
#         else:
#             return redirect('/')

@login_required(login_url='/users/login')
def update(request, bid) :
    post = Video.objects.get(Q(id=bid))  #게시글 하나를 가져오는것

    if request.user != post.writer:
        return render(request, 'Video/list.html')

    if request.method == "GET" :
        videoForm = VideoForm(instance=post)
        #특정 조건 id에 해당하는 값을 저장한다.
        return render(request,'Video/update.html',{'videoForm' : videoForm})
    elif request.method == "POST" :
        videoForm = VideoForm(request.POST, request.FILES)

        # boardForm에서 사용자가 보내온 데이터를 받느다
        if videoForm.is_valid():   #boardForm안에 값이 유효한다면
            post.title = videoForm.cleaned_data['title']
            post.tag = videoForm.cleaned_data['tag']
            post.file = videoForm.cleaned_data['file']
            post.file2 = videoForm.cleaned_data['file2']
            post.save()
            return redirect('/Video/list')

            # return render(request, 'Video/list.html',)


# def update(request, bid):
#     post = Video.objects.get(Q(id=bid))  # 게시글 하나를 가져오는것
#     if request.user != post.writer:
#         return render(request, 'Video/list.html')
#     post.delete()
#     if request.method == "GET":
#         # boardForm = BoardForm()      #입력칸에 아무것도 없는 상태로 준다
#         videoForm = VideoForm(instance=post)  # 입력칸에 아무것도 없는 상태로 준다
#         return render(request, 'video/update.html', {'videoForm': videoForm})
#     elif request.method == "POST":
#         videoForm = VideoForm(request.POST)
#         # boardForm에서 사용자가 보내온 데이터를 받느다
#         if videoForm.is_valid():  # boardForm안에 값이 유효한다면
#             post.title = videoForm.cleaned_data['title']
#             post.tag = videoForm.cleaned_data['tag']
#             post.file = videoForm.cleaned_data['file']
#
#             post.save()
#             # return redirect('/board/read/' + str(bid))
#             return redirect('/Video/list')

def requestapi1(request):
    return render(request, 'Video/test5.html')