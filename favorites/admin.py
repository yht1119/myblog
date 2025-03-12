from django.contrib import admin
from .models import Favorite, Like  # 导入 Favorite 和 Like 模型

# 注册收藏模型
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'created_at']  # 显示用户、文章和创建时间
    readonly_fields = ['user', 'article', 'created_at']  # 将所有字段设置为只读

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.all()  # 可以根据需要自定义查询集

# 注册点赞模型
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'created_at']  # 显示用户、文章和创建时间
    readonly_fields = ['user', 'article', 'created_at']  # 将所有字段设置为只读

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.all()  # 可以根据需要自定义查询集
