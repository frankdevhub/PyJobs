#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：district.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/18 10:35
"""

import inspect
from enum import Enum, unique

@unique
class DefaultDistrict(Enum):
    # 默认是上海地区的枚举类
    def __new__(cls, args):
        instance = object.__new__(cls)
        instance.en_name = args['en_name']  # 辖区英语简称
        instance.cn_name = args['cn_name']  # 辖区中文简称
        instance.district_code = args['district_code']  # 辖区区域代码
        return instance

    HP = {'en_name': 'HP', 'cn_name': '黄浦', 'district_code': 310101}  # 上海市-黄浦区
    SJ = {'en_name': 'SJ', 'cn_name': '松江', 'district_code': 310102}  # 上海市-松江区
    LW = {'en_name': 'LW', 'cn_name': '卢湾', 'district_code': 310103}  # 上海市-卢湾区
    QP = {'en_name': 'QP', 'cn_name': '青浦', 'district_code': 310118}  # 上海市-青浦区
    XH = {'en_name': 'XH', 'cn_name': '徐汇', 'district_code': 310104}  # 上海市-徐汇区
    NH = {'en_name': 'NH', 'cn_name': '南汇', 'district_code': 310119}  # 上海市-南汇区
    CN = {'en_name': 'CN', 'cn_name': '长宁', 'district_code': 310105}  # 上海市-长宁区
    FX = {'en_name': 'FX', 'cn_name': '奉贤', 'district_code': 310120}  # 上海市-奉贤区
    JA = {'en_name': 'JA', 'cn_name': '静安', 'district_code': 310106}  # 上海市-静安区
    CS = {'en_name': 'CS', 'cn_name': '川沙', 'district_code': 310152}  # 上海市-川沙区
    PT = {'en_name': 'PT', 'cn_name': '普陀', 'district_code': 310107}  # 上海市-普陀区
    CM = {'en_name': 'CM', 'cn_name': '崇明', 'district_code': 310230}  # 上海市-崇明区
    ZB = {'en_name': 'ZB', 'cn_name': '闸北', 'district_code': 310108}  # 上海市-闸北区
    HK = {'en_name': 'HK', 'cn_name': '虹口', 'district_code': 310109}  # 上海市-虹口区
    YP = {'en_name': 'YP', 'cn_name': '杨浦', 'district_code': 310110}  # 上海市-杨浦区
    MH = {'en_name': 'MH', 'cn_name': '闵行', 'district_code': 310112}  # 上海市-闵行区
    BS = {'en_name': 'BS', 'cn_name': '宝山', 'district_code': 310113}  # 上海市-宝山区
    JD = {'en_name': 'JD', 'cn_name': '嘉定', 'district_code': 310114}  # 上海市-嘉定区
    PD = {'en_name': 'PD', 'cn_name': '浦东', 'district_code': 310115}  # 上海市-浦东新区
    JS = {'en_name': 'JS', 'cn_name': '金山', 'district_code': 310116}  # 上海市-金山区


if __name__ == '__main__':
    for enum_instance in DefaultDistrict.__members__:
        print(f'{enum_instance}')
        for (type_name, obj) in inspect.getmembers(enum_instance):
            print(f'type_name: {type_name}, obj: {obj}')
