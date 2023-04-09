#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：parser.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/18 14:47
"""

import logging as log

from ...tools.date import DateUnit
from ...tools.unit import NumericUnit

log.basicConfig(level=log.INFO)

__all__ = ['parse_salary_text', 'convert_context', 'convert_data']

def is_unit_by_thousand(text):
    try:
        unit = NumericUnit(text.strip())
    except ValueError as e:
        log.error(str(e))
        return False
    if unit == NumericUnit.Thousand_CN_TW or unit == NumericUnit.Thousand:
        return True
    else:
        return False

def is_unit_by_ten_thousand(text):
    try:
        unit = NumericUnit(text.strip())
    except ValueError as e:
        log.error(str(e))
        return False
    if unit == NumericUnit.Ten_Thousand_CN \
            or unit == NumericUnit.Ten_Thousand_TW \
            or unit == NumericUnit.Ten_Thousand_EN:
        return True
    else:
        return False

def is_unit_by_day(text):
    try:
        unit = DateUnit(text.strip())
    except ValueError as e:
        log.error(str(e))
        return False
    if unit == DateUnit.DAY_1 or unit == DateUnit.DAY_2:
        return True
    else:
        return False

def is_unit_by_month(text):
    try:
        unit = DateUnit(text.strip())
    except ValueError as e:
        log.error(str(e))
        return False
    if unit == DateUnit.MONTH:
        return True
    else:
        return False

def is_unit_by_year(text):
    try:
        unit = DateUnit(text.strip())
    except ValueError as e:
        log.error(str(e))
        return False
    if unit == DateUnit.YEAR:
        return True
    else:
        return False
