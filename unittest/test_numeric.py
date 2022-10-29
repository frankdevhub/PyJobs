#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_numeric.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/2/19 19:06
"""
import inspect
import logging as log
import unittest

from ..tools.numeric import NumericUnit

log.basicConfig(level=log.DEBUG)


class TestNumericUnit(unittest.TestCase):

    def test_numeric_unit_members(self):
        log.debug('invoke method -> test_numeric_unit_members()')
        for instance in NumericUnit.__members__:
            print(f'{instance}')
            for (type_name, obj) in inspect.getmembers(instance):
                print(f'type_name: {type_name}, obj: {obj}')


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestNumericUnit('test_numeric_unit_members'))  # test_numeric_unit_members
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
