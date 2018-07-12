#!/usr/bin/env python
__author__ = 'Albino'

from django.contrib.auth.mixins import LoginRequiredMixin as _LoginRequiredMixin

class LoginRequiredMixin(_LoginRequiredMixin):
    """
    登录权限
    """
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
