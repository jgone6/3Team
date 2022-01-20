from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Member.forms import MemberForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
from Member.models import Member


def signup(request) :
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/register.html', {'signupForm' : signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        memberForm = MemberForm(request.POST)
        if signupForm.is_valid() :
            user = signupForm.save()
            member = memberForm.save(commit=False)
            member.user = user
            member.save()
            return redirect('/users/register')


def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login_page.html',
                      {'loginForm':loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid() :
            print('로그인 성공')
            login(request, loginForm.get_user())
            return redirect('/')
        else :
            print('로그인 실패')
            return redirect('/users/login')


def logout(request):
    logout(request)
    return redirect('/users/login_page')

def findID(request):
    if request.method == "GET":
        return render(request, 'users/forget_ID.html')
    elif request.method == "POST":
        # 값 전달 받음
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        print(nickname)
        print(phone)
        # member와 user 테이블을 조인해서 조회
        if member = Member.objects.select_related('user').get(Q(nickname=nickname) & Q(phone=phone)) :
            print(member.user.username)
        else :
                return render(request, 'users/error.html')
return render(request, 'users/forget_ID.html')






def findPassword(request):
    return render(request, 'users/forget_password.html')

def announceID(request):
    return render(request,'users/announce.html')


def addinfo(request) :
        if request.method == "GET":
            memberForm = MemberForm()
            return render(request, 'users/addinfo.html',
                          {'memberForm': memberForm})
        elif request.method == "POST":
            memberForm = MemberForm(request.POST)

        if memberForm.is_valid():
            member = memberForm.save(commit=False)
            member.nickname = memberForm.cleaned_data['nickname']
            member.phone = memberForm.cleaned_data['phone']
            member.save()
            return redirect('/users/login')

