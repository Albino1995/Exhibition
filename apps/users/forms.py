#!/usr/bin/env python
__author__ = 'Albino'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required':'请输入用户'})
    password = forms.CharField(required=True, error_messages={'required':'请输入密码'})


class MessageForm(forms.Form):
    mobile = forms.CharField(required=True, max_length=20, error_messages={'required': '请输入联系方式',
                                                                           'max_length': '联系方式请勿长于20字'}
                             )

    message = forms.CharField(required=True, max_length=200, error_messages={'required': '请输入意见或建议',
                                                                            'max_length': '意见或建议请勿长于200字'}
                              )