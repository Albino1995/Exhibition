import time
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Reservation(models.Model):
    """
    预约
    """
    user = models.ForeignKey(User, verbose_name='用户')
    department = models.CharField(max_length=20, verbose_name='预约部门')
    applicant = models.CharField(max_length=10, verbose_name='预约者')
    date = models.DateField(default=time.strftime("%Y-%m-%d", time.localtime()),
                            verbose_name='预约日期')
    field = models.CharField(default='9:00 - 12:00',
                             choices=(('9:00 - 12:00', '9:00 - 12:00'),
                                      ('14:00 - 17:00', '14:00 - 17:00')),
                             max_length=30, verbose_name='场次')
    type = models.CharField(default='待审核',
                            choices=(('待审核', '待审核'),
                                     ('已预约', '已预约'),
                                     ('已完成', '已完成')),
                            max_length=10, verbose_name='场次状态')
    client_name = models.CharField(max_length=50, verbose_name='客户名称')
    client_level = models.CharField(max_length=10, verbose_name='客户级别')
    mobile = models.CharField(max_length=20, verbose_name='预约者联系方式')
    remarks = models.TextField(default='', verbose_name='备注', blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '展厅场次'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {} 场次'.format(str(self.date), self.field)

    def expired_or_not(self):
        """
        是否已完成
        """
        _date = str(self.date).split('-')
        d1 = datetime.now()
        d2 = datetime(int(_date[0]), int(_date[1]), int(_date[2]))
        result = (d2 - d1).days
        if result >= 0:
            return self.type
        else:
            self.type = '已完成'
            self.save()
            return self.type


class Evaluation(models.Model):
    """
    评价
    """
    reservation = models.ForeignKey(Reservation, verbose_name='预约记录')
    evaluation = models.CharField(choices=(('满意', '满意'), ('一般', '一般'), ('不满意', '不满意')),
                                  default='满意',
                                  max_length=10,
                                  verbose_name='服务评价')
    remarks = models.TextField(default='', verbose_name='备注', blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '服务评价'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}的评价'.format(self.reservation)
