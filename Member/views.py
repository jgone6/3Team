from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from Member.forms import MemberForm
from Member.models import Member
import requests


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
            return redirect('/')
        else:
            print('로그인 실패')
            return redirect('/users/error')


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
            return redirect('/users/register')


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
        try:
            user = Member.objects.get(Q(nickname=nickname))
        except Member.DoesNotExist:  # 에러 종류
            return render(request, 'users/error.html')
        if phone == user.phone:
            member = Member.objects.select_related('user').get(Q(nickname=nickname) & Q(phone=phone))
            return render(request, 'users/forget_password.html', {'member': member})
        else:
            return render(request, 'users/error.html')


# 패스워드 변경하기
from django.contrib import auth

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
        return redirect('/users/login')
        return redirect('/')


# 오류페이지
def error(request):
    return render(request, 'users/error.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# 카카오 회원가입
def request_api2(request):
    return redirect("https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=96e603d6c4c66606ae14132233e73702&redirect_uri=http://127.0.0.1:8000/kakaosignup")

def kakao_signup(request):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "authorization_code",
            "client_id": "96e603d6c4c66606ae14132233e73702",
            "redirect_uri": "http://127.0.0.1:8000/kakaosignup",
            "code": request.GET.get('code')}

    res = requests.post("https://kauth.kakao.com/oauth/token",
                        data=data,
                        headers=headers)
    access_token = res.json()['access_token']
    print(access_token)

    kakao_user_info = requests.post("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}, ).json()
    kakaoid = kakao_user_info.get('id', None)
    kakaoid = int(kakaoid)
    kakaoaccounts = kakao_user_info.get('kakao_account')
    kakaoproperties = kakao_user_info.get('properties')
    kakaonickname = kakaoproperties.get('nickname')
    kakaoemail = kakaoaccounts.get('email')

    user = User()
    user.email = kakaoemail
    user.username = kakaonickname
    user.is_active = True
    user.save()

    return redirect('/users/login')


# 카카오 로그인
def request_api3(request):
    return redirect("https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=96e603d6c4c66606ae14132233e73702&redirect_uri=http://127.0.0.1:8000/kakaologin")

def kakao_login(request):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "authorization_code",
            "client_id": "96e603d6c4c66606ae14132233e73702",
            "redirect_uri": "http://127.0.0.1:8000/kakaologin",
            "code": request.GET.get('code')}

    res = requests.post("https://kauth.kakao.com/oauth/token",
                        data=data,
                        headers=headers)
    access_token = res.json()['access_token']
    print(access_token)

    kakao_user_info = requests.post("https://kapi.kakao.com/v2/user/me",
                                    headers={"Authorization": f"Bearer {access_token}"}, ).json()
    kakaoid = kakao_user_info.get('id', None)
    kakaoid = int(kakaoid)
    kakaoaccounts = kakao_user_info.get('kakao_account')

    kakaoemail = kakaoaccounts.get('email')
    print(kakaoemail)

    user = User.objects.get(Q(email=kakaoemail))
    print(user)

    login(request, user)
    return redirect('/')

# 연결끊기
def kakao_logout(request):
    return redirect("https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=96e603d6c4c66606ae14132233e73702&redirect_uri=http://127.0.0.1:8000/users/kakaologout2")

def kakao_logout2(request):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "authorization_code",
            "client_id": "96e603d6c4c66606ae14132233e73702",
            "redirect_uri": "http://127.0.0.1:8000/users/kakaologout2",
            "code": request.GET.get('code')}

    res = requests.post("https://kauth.kakao.com/oauth/token",
                        data=data,
                        headers=headers)
    access_token = res.json()['access_token']

    return render(request, 'users/unlink.html', {'access_token': access_token})

# 회워가입 선택
def signup_method(request):
    return render(request, 'users/signup_method.html')

# 로그아웃 선택
def logout_method(request):
    return render(request, 'users/logout_method.html')

# 로그인 선택
def login_method(request):
    return render(request, 'users/login_method.html')