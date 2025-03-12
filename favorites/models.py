from django.db import models
from user.models import MyUser
from article.models import Article  # 确保导入 Article 模型

class Favorite(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)  # 使用 MyUser 作为用户模型
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 使用 Article 作为文章模型
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')  # 防止重复收藏
        verbose_name = '收藏管理'  # 设置单数名称
        verbose_name_plural = '收藏管理'  # 设置复数名称

    def __str__(self):
        return f"{self.user.username} 收藏了 {self.article.title}"

class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')  # 防止重复点赞
        verbose_name = '点赞管理'  # 设置单数名称
        verbose_name_plural = '点赞管理'  # 设置复数名称

    def __str__(self):
        return f"{self.user.username} 点赞了 {self.article.title}"
