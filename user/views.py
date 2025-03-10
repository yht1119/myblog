import django
from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib.auth import login as auth_login, logout, authenticate
from django.urls import reverse


def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    password2 = request.POST.get('password2', '')
    
    # 检查用户名是否已存在
    if MyUser.objects.filter(username=username).exists():
        info = '用户已存在！'
    # 检查两次输入的密码是否一致
    elif password2 != password:
        info = '两次密码输入不一致！'
    else:
        # 创建普通用户
        user = MyUser.objects.create_user(
            username=username, 
            password=password,
            is_superuser=False,  # 设置为普通用户
            is_staff=False       # 设置为普通用户
        )
        user.save()
        info = '注册成功，请重新登录'
        logout(request)
    
    return render(request, 'register.html', {'info': info})


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    # 检查用户是否存在
    if MyUser.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                kwargs = {'id': request.user.id, 'page': 1, 'typeId': 0}
                return redirect(reverse('article', kwargs=kwargs))
            else:
                errorinfo = '用户未激活！'
        else:
            errorinfo = '用户名或者密码错误！'
    else:
        errorinfo = '用户不存在，请注册'
    
    return render(request, 'login.html', {'errorinfo': errorinfo})


def toLoginPage(request):
    """跳转登录页面"""
    return render(request, 'login.html')


def toRegisterPage(request):
    """跳转到注册页面"""
    return render(request, 'register.html')


def about(request, id):
    """根据用户id查询个人信息"""
    user = MyUser.objects.filter(id=id).first()
    return render(request, 'about.html', locals())
