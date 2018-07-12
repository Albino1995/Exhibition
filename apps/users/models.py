from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    """
    意见收集
    """
    user = models.ForeignKey(User, verbose_name='填写人')
    mobile = models.CharField(blank=True, null=True, max_length=20, verbose_name='联系方式')
    message = models.TextField(default='', verbose_name='用户意见')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '意见收集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}的意见'.format(self.user)
