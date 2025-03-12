import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from article.models import Article, Comment
from favorites.models import Favorite, Like
from user.models import MyUser


# Create your views here.

def article(request, id, page, typeId):
    """
    根据页码查询帖子
    :param request:
    :param id:
    :param page:
    :param typeId: 0表示查询全部
    :return:
    """
    pageSize = 10  # 每页大小
    user = MyUser.objects.filter(id=id).first()
    admin_user_id = 2  # 管理员用户的ID为2
    if not user:
        return redirect(reverse('toRegisterPage'))
    if typeId == None or typeId == 0:
        articleList = Article.objects.filter(author_id=admin_user_id).order_by('-create_time')
    else:
        articleList = Article.objects.filter(author_id=admin_user_id, type_id=typeId).order_by('-create_time')
    paginator = Paginator(articleList, pageSize)
    try:
        pageData = paginator.page(page)  # 获取一页数据
    except PageNotAnInteger:
        pageData = paginator.page(1)  # 如果前端传来的页码不是整型，则返回第一页数据
    except EmptyPage:
        pageData = paginator.page(paginator.num_pages)  # 如果前端传来的页码超过实际页数，则返回最后一页数据
    return render(request, 'article.html', locals())


def detail(request, id, aId):
    """
    根据用户id和帖子id查看详细信息 & 添加评论信息
    :param request:
    :param id:
    :param aId:
    :return:
    """
    if request.method == 'GET':  # 查询帖子信息
        user = MyUser.objects.filter(id=id).first()
        article = get_object_or_404(Article, id=aId)
        # 阅读量加1
        Article.objects.filter(id=aId).update(reads=F('reads') + 1)
        # 获取博客评论信息
        commentList = Comment.objects.filter(article_id=aId).order_by('-create_time')
        # 获取当前用户的收藏
        is_favorited = Favorite.objects.filter(user=user, article=article).exists()  # 检查是否已收藏
        # 获取当前用户的点赞
        is_liked = Like.objects.filter(user=user, article=article).exists()  # 检查是否已点赞
        return render(request, 'detail.html', locals())
    else:  # 添加评论信息
        user = MyUser.objects.filter(id=id).first()
        content = request.POST.get("content")
        value = {'user': user, 'content': content, 'article_id': aId, 'create_time': datetime.datetime.now(),
                 'author_id': id}
        Comment.objects.create(**value)
        kwargs = {'id': id, 'aId': aId}
        return redirect(reverse('detail', kwargs=kwargs))


def search(request, id):
    """
    根据搜索条件搜索指定用户帖子，只显示前10条记录
    :param request:
    :param id:
    :param v:
    :return:
    """
    v = request.POST.get("v")
    admin_user_id = 2  # 管理员用户的ID为2
    articleList = Article.objects.filter(Q(author_id=admin_user_id, title__contains=v) | Q(author_id=admin_user_id, content__contains=v))
    paginator = Paginator(articleList, 10)
    pageData = paginator.page(1)
    return render(request, 'result.html', locals())
