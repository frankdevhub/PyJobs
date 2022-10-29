#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：date.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/18 10:13
"""
import inspect
from enum import Enum, unique

date_units = {'day_1': '天', 'day_2': '日', 'month': '月', 'year': '年'}

@unique
class DateUnit(Enum):
    # 通用时间单位
    def __new__(cls, name: str):
        instance = object.__new__(cls)
        instance.unit = date_units.get(name)
        return instance

    DAY_1 = 'day_1'  # DAY_1
    DAY_2 = 'day_2'  # DAY_2
    MONTH = 'month'  # MONTH
    YEAR = 'year'  # YEAR


if __name__ == '__main__':
    for enum_instance in DateUnit.__members__:
        print(f'{enum_instance}')
        for (type_name, obj) in inspect.getmembers(enum_instance):
            print(f'type_name: {type_name}, obj: {obj}')
