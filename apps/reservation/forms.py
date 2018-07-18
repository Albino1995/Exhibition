#!/usr/bin/env python
__author__ = 'Albino'

from django import forms


class ReservationForm(forms.Form):
    date = forms.DateField(required=True, error_messages={'required': '请选择日期'})
    field = forms.CharField(required=True, error_messages={'required': '请选择场次'})
    client_name = forms.CharField(required=True, max_length=50, error_messages={'required': '请输入客户名称',
                                                                                'max_length': '客户名称请勿长于50字节'}
                                  )
    client_level = forms.CharField(required=True, max_length=10, error_messages={'required': '请输入客户级别',
                                                                                 'max_length': '客户等级请勿长于10字节'}
                                   )
    department = forms.CharField(required=True, max_length=20, error_messages={'required': '请输入预约部门',
                                                                               'max_length': '预约部门请勿长于20字节'}
                                 )
    applicant = forms.CharField(required=True, max_length=10, error_messages={'required': '请输入预约者',
                                                                              'max_length': '预约者请勿长于10字节'}
                                )
    mobile = forms.CharField(required=True, max_length=20, error_messages={'required': '请输入预约者联系方式',
                                                                           'max_length': '联系方式请勿长于20字节'}
                             )
    remarks = forms.CharField(required=False)