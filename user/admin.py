from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.unregister(Group)
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 
                    'name', 'introduce',
                    'company', 'profession',
                    'address', 'telephone',
                    'wx', 'qq', 'avatar']


    def get_queryset(self, request):
        qs = super(MyUserAdmin, self).get_queryset(request)
        return qs.all()

    def get_readonly_fields(self, request, obj=None):
        # 设置除了 'id' 和 'username' 以外的所有字段为只读
        if obj:  # 如果是编辑现有用户
            return ['name', 'introduce', 'company', 'profession', 'address', 'telephone', 'wx', 'qq', 'avatar']
        return []  # 如果是添加新用户，所有字段都可编辑

    def has_change_permission(self, request, obj=None):
        # 禁止修改用户信息
        return False

    def has_view_permission(self, request, obj=None):
        # 允许查看用户信息
        return True

    def has_delete_permission(self, request, obj=None):
        # 允许删除用户
        return True

    def has_add_permission(self, request):
        # 允许添加用户
        return True
