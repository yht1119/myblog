from django.shortcuts import get_object_or_404, redirect, render
from article.models import Article
from user.models import MyUser
from .models import Favorite, Like

def add_to_favorites(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.is_authenticated:  # 检查用户是否登录
        Favorite.objects.get_or_create(user=request.user, article=article)
    return redirect('detail', id=request.user.id, aId=article.id)

def remove_from_favorites(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.is_authenticated:  # 检查用户是否登录
        favorite = Favorite.objects.filter(user=request.user, article=article)
        if favorite.exists():
            favorite.delete()
    return redirect('detail', id=request.user.id, aId=article.id)

def add_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.is_authenticated:
        Like.objects.get_or_create(user=request.user, article=article)
    return redirect('detail', id=request.user.id, aId=article.id)

def remove_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.is_authenticated:
        like = Like.objects.filter(user=request.user, article=article)
        if like.exists():
            like.delete()
    return redirect('detail', id=request.user.id, aId=article.id)

def my_favorites(request, id):
    user = get_object_or_404(MyUser, id=id)  # 根据 ID 获取用户
    favorites = Favorite.objects.filter(user=user)  # 查询该用户的收藏
    return render(request, 'my_favorites.html', locals())
