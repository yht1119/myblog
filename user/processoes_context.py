from user.models import MyUser

def user_identity(request):
    """
    返回当前用户的身份信息
    :param request:
    :return: 布尔值，管理员为 True，一般用户为 False，未登录为 None
    """
    if request.user.is_authenticated:
        return {
            'user_identity': request.user.is_staff  # 管理员为 True，一般用户为 False
        }
    return {
        'user_identity': None  # 未登录用户返回 None
    }
