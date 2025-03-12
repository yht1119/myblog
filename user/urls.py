from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views

# 路由
urlpatterns = [

    # 用户登录请求
    path('login', login, name='userLogin'),
    # 跳转登录页面
    path('login.html', toLoginPage, name='toLoginPage'),
    # 跳转注册页面
    path('register.html', toRegisterPage, name='toRegisterPage'),
    # 用户注册请求
    path('register', register, name='userregister'),
    # 关于博主
    path('about/<int:id>/.html', about, name='about'),
    path('edit_user/<int:id>/.html', edit_user, name='edit_user'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('password_change_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    # 注销
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
]
