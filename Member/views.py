from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def signup(request) :
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/register.html',
                                {'signupForm' : signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid() :
            signupForm.save()

            return redirect('/users/register')


def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login_page.html',
                      {'loginForm':loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid() :
            login(request, loginForm.get_user())
            return redirect('/board/list')
        else :
            return redirect('/users/login_page')

def logout(request):
    logout(request)
    return redirect('/users/login_page')

def findID(request):

    return render(request, 'users/forget_ID.html')

def findPassword(request):

    return render(request, 'users/forget_password.html')

def announceID(request):

    return render(request,'users/announce.html')