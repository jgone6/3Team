from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm

from Member.forms import MemberForm
from Member.models import Member
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.

# 로그인

def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login_page.html',
                      {'loginForm': loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            print('로그인 성공')
            login(request, loginForm.get_user())
            # return redirect('/Video/list')
            return redirect('/Video/list')
        else:
            print('로그인 실패')
            # return redirect('/users/login')
            return redirect('/users/login')

# 회원가입
def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/register.html', {'signupForm': signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        memberForm = MemberForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save()
            member = memberForm.save(commit=False)
            member.user = user
            member.save()
            # return redirect('/users/register')
            return redirect('/users/login')


# ID 찾기
def findID(request):
    if request.method == "GET":
        return render(request, 'users/forget_ID.html')


# 패스워드 찾기
def findPassword(request):
    if request.method == "GET":
        return render(request, 'users/forget_password.html')
    elif request.method == "POST":
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        phone1 = Member.objects.get(Q(nickname=nickname))
        print(phone1.phone)
        if phone == phone1.phone:
            member = Member.objects.select_related('user').get(Q(nickname=nickname) & Q(phone=phone))
            return render(request, 'users/forget_password.html', {'member': member})
        else:
            return render(request, 'users/error_ID.html')


# 패스워드 변경하기
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth

def changePassword(request):
    if request.method == "GET":
        username = request.GET.get('username', None)
        return render(request, 'users/change_password.html', {'username' : username})
    elif request.method == "POST":
        print(request.POST)
        username = request.POST.get('username', None)
        user = User.objects.get(username=username)

        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
        print("비밀번호를 성공적으로 변경하였습니다.")
        return redirect('/')



        # phone = request.POST.get('phone')
        # user_password = request.POST.get('new_password')
        # print(phone)
        # member = Member.objects.select_related('user').get(Q(phone=phone))
        # print(member.user.password)
        # member.user.password = user_password
        # print(member.user.password)
        # member.user.save()
        return redirect('/')


# 오류페이지
def error_ID(request):
    return render(request, 'users/error_ID.html')


def error_password(request):
    return render(request, 'users/error_password.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    # return HttpResponseRedirect('/users/login')
    return HttpResponseRedirect('/users/login')
