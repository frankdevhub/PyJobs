# !/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: test_django_orm.py
# @time: 2021/2/16 12:03

import logging as log
import os
import unittest

import django

from ..models.models import BlogDocumentBrief

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_sites.settings')
django.setup()

log.basicConfig(level=log.DEBUG)

class DjangoORMTest(unittest.TestCase):

    @staticmethod
    def test_insert():
        # 测试新增博客文档对象
        log.debug('invoke method -> test_insert()')
        obj = BlogDocumentBrief('', 'blog_domain', 'doc_title')
        obj.save()

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(DjangoORMTest('test_insert'))  # test_insert 测试新增对象
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
