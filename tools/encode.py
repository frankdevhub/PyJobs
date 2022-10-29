#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：encode.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/16 20:49
"""
import inspect
from enum import Enum, unique

@unique
class CharacterEncode(Enum):
    # 通用国际字符编码
    def __new__(cls, name: str):
        instance = object.__new__(cls)
        instance.code_name = name
        return instance

    GB2312 = 'GB2312'  # GB2312
    ASCII = 'ASCII'  # ASCII
    MBCS = 'MBCS'  # MBCS
    GBK = 'GBK'  # GBK
    Big5 = 'Big5'  # Big5
    Unicode = 'Unicode'  # Unicode
    UTF8 = 'UTF8'  # UTF8
    Base64 = 'Base64'  # Base64


if __name__ == '__main__':
    for enum_instance in CharacterEncode.__members__:
        print(f'{enum_instance}')
        for (type_name, obj) in inspect.getmembers(enum_instance):
            print(f'type_name: {type_name}, obj: {obj}')
