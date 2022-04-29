"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import Video.views
import Member.views
import Comment.views


urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('Video/upload', Video.views.upload),
                  path('Video/list', Video.views.posts),
                  path('Video/mylist', Video.views.myposts),
                  path('Video/test2', Video.views.test2),
                  path('Video/tag/<str:tags>', Video.views.getTag),
                  path('Video/list/music', Video.views.list_music),
                  path('Video/list/var', Video.views.list_var),
                  path('Video/list/geo', Video.views.list_geo),
                  path('Video/list/edu', Video.views.list_edu),
                  path('Video/read/<int:bid>', Video.views.read),
                  path('Video/delete/<int:bid>', Video.views.delete),
                  path('Video/update/<int:bid>', Video.views.update),
                  path('Video/readmine/<int:bid>', Video.views.readmine),
                  path('', Video.views.ss),
                  path('users/login', Member.views.userlogin),
                  path('users/logout', Member.views.logout),
                  path('users/register', Member.views.signup),
                  path('users/forgetID', Member.views.findID),
                  path('users/forgetpassword', Member.views.findPassword),
                  path('users/changepassword', Member.views.changePassword),
                  path('users/error', Member.views.error),
                  path('users/request_api2', Member.views.request_api2),
                  path('users/request_api3', Member.views.request_api3),
                  path('users/kakaologout', Member.views.kakao_logout),
                  path('users/kakaologout2', Member.views.kakao_logout2),
                  path('kakaologin', Member.views.kakao_login),
                  path('kakaosignup', Member.views.kakao_signup),
                  path('users/choose_signup', Member.views.signup_method),
                  path('users/choose_logout', Member.views.logout_method),
                  path('users/choose_login', Member.views.login_method),
                  path('Video/test',Video.views.requestapi1),
                  path('Video/google',Video.views.main),
                  path('comment/write2',Comment.views.write2),
                  path('comment/list', Comment.views.comment_list),
                  path('comment/write/<int:bid>', Comment.views.write),
                  path('comment/content/<int:bid>',Comment.views.comment_content),
                  path('comment/delete/<int:bid>', Comment.views.comment_delete),
                  path('comment/update/<int:bid>', Comment.views.comment_update),







                  # path('Video/get_service',Video.views.get_service),
                  # path('Video/get_first_profile_id',Video.views.get_first_profile_id),
                  #
                  #
                  # path('Video/get_results',Video.views.get_results),
                  # path('Video/print_results',Video.views.print_results),







              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
