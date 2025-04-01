import django
from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib.auth import login as auth_login, logout, authenticate
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

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
    return render(request, 'register.html', locals())


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    # 检查用户是否存在
    if MyUser.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                django.contrib.auth.login(request, user)
            kwargs = {'id': request.user.id, 'page': 1, 'typeId': 0}
            return redirect(reverse('article', kwargs=kwargs))
        else:
            errorinfo = '用户名或者密码错误！'
    else:
        errorinfo = '用户不存在，请注册'
    return render(request, 'login.html', locals())


def toLoginPage(request):
    """跳转登录页面"""
    return render(request, 'login.html')


def toRegisterPage(request):
    """跳转到注册页面"""
    return render(request, 'register.html')


def about(request, id):
    """
    根据用户id查询个人信息
    :param request:
    :param id:
    :return:
    """
    user = MyUser.objects.filter(id=id).first()
    return render(request, 'about.html', locals())

def edit_user(request, id):
    """
    修改个人信息
    """
    user = get_object_or_404(MyUser, id=id)
    if request.method == 'POST':
        # 获取表单数据并更新用户信息
        user.name = request.POST.get('name')
        user.introduce = request.POST.get('introduce')
        user.company = request.POST.get('company')
        user.profession = request.POST.get('profession')
        user.wx = request.POST.get('wx')
        user.qq = request.POST.get('qq')
        user.telephone = request.POST.get('telephone')
        user.address = request.POST.get('address')
        
        # 处理头像上传
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            user.avatar.save(avatar.name, avatar, save=True)
        
        user.save()
        return redirect('about', id=user.id)
    return render(request, 'edit_user.html', locals())

def upload_background(request, id):
    """
    上传背景图像
    """
    user = get_object_or_404(MyUser, id=id)
    if request.method == 'POST':
        # 处理背景图像上传
        if 'background_image' in request.FILES:
            background_image = request.FILES['background_image']
            user.background_image.save(background_image.name, background_image, save=True)
        return redirect('article', id=user.id, page=1, typeId=0)
    return render(request, 'upload_background.html', locals())

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'  # 自定义模板
    success_url = reverse_lazy('password_change_done')  # 修改成功后的重定向 URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # 将当前用户信息传递给模板
        return context

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'  # 自定义成功提示模板

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # 将当前用户信息传递给模板
        return context

