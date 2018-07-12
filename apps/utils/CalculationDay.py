#!/usr/bin/env python
__author__ = 'Albino'

from datetime import datetime


def calculation_date(date):
    _date = date.split('-')
    d1 = datetime.now()
    d2 = datetime(int(_date[0]), int(_date[1]), int(_date[2]))
    result = (d2 - d1).days
    if result < 0:
        return '请选择合法的日期'
    if result > 14:
        return '请选择当天至之后14天内的日期'
    return ''


def serialize_date(date):
    _date = date.split('-')
    res = []
    for d in _date:
        if d.startswith('0'):
            d = d[1:]
        res.append(d)
    return '{}年{}月{}日'.format(res[0], res[1], res[2])
