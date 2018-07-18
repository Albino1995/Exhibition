#!/usr/bin/env python
__author__ = 'Albino'

import xadmin
from xadmin import views

from .models import Message

class MessageAdmin:
    list_display = ['user', 'mobile', 'add_time']
    list_filter = ['user', 'mobile', 'add_time']
    search_fields = ['user', 'message']


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '展厅预约后台管理'
    site_footer = '展厅预约后台管理'

xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)