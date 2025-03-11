from django.contrib import admin
from article.models import *

# Register your models here.


admin.site.site_title = "个性化博客后台管理"
admin.site.index_title = "博客后台管理"
admin.site.site_header = "个性化博客管理系统"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image', 'create_time', 'abstract']

    def get_queryset(self, request):
        """
        查询过滤
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        return qs.filter(author_id=request.user.id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        新增或修改数据时，设置外键可选值
        :param db_field:
        :param request:
        :param kwargs:
        :return:
        """
        if db_field.name == 'author':
            # 只允许当前用户作为作者
            kwargs["queryset"] = MyUser.objects.filter(id=request.user.id)
        if db_field.name == 'type':
            kwargs["queryset"] = ArticleType.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        # 将 author 字段设置为只读
        return ['author']

    def save_model(self, request, obj, form, change):
        # 在保存模型时，自动设置作者为当前用户
        if not change:  # 只有在添加新文章时
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    def get_queryset(self, request):
        """
        查询过滤
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        return qs.all()



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'user', 'content', 'create_time']

    def get_queryset(self, request):
        """
        查询过滤
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        return qs.all()

    def get_readonly_fields(self, request, obj=None):
        # 将所有字段设置为只读
        return ['article', 'user', 'content', 'create_time', 'id']  # 添加所有需要只读的字段

    def has_change_permission(self, request, obj=None):
        # 禁止修改评论
        return False

    def has_add_permission(self, request):
        # 禁止添加新评论
        return False

    def has_delete_permission(self, request, obj=None):
        # 允许删除评论
        return True
