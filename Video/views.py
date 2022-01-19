from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Video.forms import VideoForm
from Video.models import Video


def ss(request):

    return render(request, 'Video/ss.html')


def register(request):
    if request.method == "GET":
        videoForm = VideoForm()  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'video/register.html',
                      {'videoForm': videoForm})
    # render라는 함수가 boardForm의 데이터 board폴더에 forms.py 안에 있는 데이터  받아와 board/register3.html을 완성시킨다는 개념

    elif request.method == "POST":
        videoForm = VideoForm(request.POST)
        # 모델폼을 이용하면 알아서 다 받아짐
        if videoForm.is_valid():  # boardForm안에 값이 유효한다면
            video = videoForm.save(commit=False)
            # board.writer = request.user
            video.save()
            return redirect('/video/list')

def posts(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list.html',
                  {'posts': posts})