#!/usr/bin/env python
__author__ = 'Albino'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required':'请输入用户'})
    password = forms.CharField(required=True, error_messages={'required':'请输入密码'})


class MessageForm(forms.Form):
    mobile = forms.CharField(required=True, error_messages={'required': '请输入联系方式'})
    message = forms.CharField(required=True, error_messages={'required': '请输入意见或建议'})