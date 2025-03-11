from django.contrib import admin

from message.models import Message


# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'create_time', 'user']

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
        return ['content', 'create_time', 'user']

    def has_change_permission(self, request, obj=None):
        # 禁止修改消息
        return False

    def has_add_permission(self, request):
        # 禁止添加新消息
        return False

    def has_delete_permission(self, request, obj=None):
        # 允许删除消息
        return True

    def add_view(self, request, form_url='', extra_context=None):
        """
        设置下拉框默认选中
        :param request:
        :param form_url:
        :param extra_context:
        :return:
        """
        data = request.GET.copy()
        data['user'] = request.user
        request.GET = data
        return super(MessageAdmin, self).add_view(request, form_url, extra_context)
