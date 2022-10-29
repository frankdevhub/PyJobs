#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_models_orm.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/9/4 17:15
"""

import logging as log
import unittest

from ..data.sqlacodegen_models import *
from ..data.sqlalchemy_orm import *

log.basicConfig(level=log.DEBUG)


class TestModelORM(unittest.TestCase):

    def test_get_session(self):
        # 测试建立数据库连接实体对象
        log.debug('invoke method -> test_get_session()')
        Session = get_session()
        session = Session()
        assert session is not None, f'variable session cannot be none'
        print(f'session = {session}')

    def test_add_document(self):
        # 测试新增实体对象
        log.debug('invoke method -> test_add_object()')
        blog_doc = BlogDocumentBrief(blog_domain='https://cloud.51cto.com/art/202109/684220.htm')
        Session = get_session()
        db_session = Session()
        assert db_session is not None, f'variable session cannot be none'
        ##
        db_session.add_all([blog_doc])
        db_session.commit()

    def test_delete_document(self):
        # 测试删除(逻辑删除)实体对象
        log.debug('invoke method -> test_delete_document()')
        pass

    def test_query_document_by_id(self):
        # 测试条件查询(依据主键)获取实体对象
        log.debug('invoke method -> test_query_document_by_id()')
        pass

    def test_update_document(self):
        # 测试更新实体对象
        log.debug('invoke method -> test_update_document()')
        pass


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # test_suite.addTest(TestModelORM('test_get_session'))  # test_get_session
    test_suite.addTest(TestModelORM('test_add_document'))  # test_add_document
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
