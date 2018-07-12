#!/usr/bin/env python
__author__ = 'Albino'

from django import forms


class ReservationForm(forms.Form):
    date = forms.DateField(required=True, error_messages={'required': '请选择日期'})
    field = forms.CharField(required=True, error_messages={'required': '请选择场次'})
    client_name = forms.CharField(required=True, error_messages={'required': '请输入客户名称'})
    client_level = forms.CharField(required=True, error_messages={'required': '请输入客户级别'})
    department = forms.CharField(required=True, error_messages={'required': '请输入预约部门'})
    applicant = forms.CharField(required=True, error_messages={'required': '请输入预约者'})
    mobile = forms.CharField(required=True, error_messages={'required': '请输入预约者联系方式'})
    remarks = forms.CharField(required=False)