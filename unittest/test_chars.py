# !/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: test_character.py
# @time: 2021/2/16 12:03

import inspect
import logging as log
import unittest

from ..tools.chars import CharacterHelper

log.basicConfig(level=log.DEBUG)

class TestCharacterHelper(unittest.TestCase):
    CHARACTER_EXAMPLE = ('1', '各', '时', '個', '詢', 's', '1', '-')

    @staticmethod
    def test_is_simple_chinese_character():
        # 测试是否是简体中文字符
        examples = TestCharacterHelper.CHARACTER_EXAMPLE
        for x in examples:
            print(type(x))
            bool_res = CharacterHelper.is_simple_chinese_character(x)
            assert isinstance(bool_res, bool)
            print(f'return value: {bool_res}')
        return True

    @staticmethod
    def test_get_instance_methods():
        # 测试获取类的函数成员变量
        instance_members = [(obj, type(obj)) for (type_name, obj) in inspect.getmembers(CharacterHelper) if
                            inspect.isfunction(obj)]
        # print(instance_members)
        test_example = "個"  # 测试使用字符

        for inst in instance_members:
            func = inst[0]
            print(f'function_name: {func.__name__} ,arg_count: {func.__code__.co_argcount}')
            fun_name = func.__name__
            if fun_name.lstrip().startswith('is_'):
                bool_res = func(test_example)
                assert isinstance(bool_res, bool)
                print(f'return value: {bool_res}')

        return True

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestCharacterHelper('test_is_simple_chinese_character'))  # test_is_simple_chinese_character
    test_suite.addTest(TestCharacterHelper('test_get_instance_methods'))  # test_get_instance_methods
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
