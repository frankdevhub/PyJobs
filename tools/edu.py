#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：education.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/19 19:22
"""
import inspect
from enum import Enum, unique

@unique
class EducationDegree(Enum):
    # 教育学历文化水平
    def __new__(cls, args):
        inst = object.__new__(cls)
        inst.name = args['name']  # 学历中文名称
        inst.code = args['code']  # 学历英文代码
        return inst

DOCTOR = {'name': '博士', 'code': 'doctor'}  # DOCTOR
MASTER = {'name': '硕士研究生', 'code': 'master'}  # MASTER
BACHELOR = {'name': '本科', 'code': 'bachelor'}  # BACHELOR
TACHNICAL_COLLEGE = {'name': '中专', 'code': 'technical_college'}  # TACHNICAL_COLLEGE

if __name__ == '__main__':
    for inst in EducationDegree.__members__:
        print(f'{inst}')
        for (type_name, obj) in inspect.getmembers(inst):
            print(f'type_name: {type_name}, obj: {obj}')
