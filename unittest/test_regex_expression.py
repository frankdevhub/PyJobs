#!/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: test_regex_expression.py
# @time: 2021/2/13 12:24
# @desc: 解析匹配的正则表达式测试

import logging as log
import re
import unittest

log.basicConfig(level=log.DEBUG)

# test_blog_doc_id_regex = '.*(?P<header>/http[s]{0,1}:\/\/([\w.]+\/?)\S*/)(?P<union_id>\/[0-9]{1,})$'
test_blog_doc_id_regex = '[0-9]{1,}$'
test_blog_doc_link = "https://blog.51cto.com/oldboy/1926142"  # docId= 1926142, 测试博客网址链接(51CTO平台)
test_blog_doc_links = ["https://blog.51cto.com/oldboy/1926142",  # docId= 1926142
                       "https://blog.51cto.com/oldboy/1884326",  # docId= 1884326
                       "https://blog.51cto.com/oldboy/1855640",  # docId= 1855640
                       "https://blog.51cto.com/oldboy/7750568",  # docId= 7750568
                       "https://blog.51cto.com/oldboy/1855461",  # docId= 1855461
                       "https://blog.51cto.com/oldboy/1911034"]  # docId= 1911034


class TestRegexExpression(unittest.TestCase):

    @staticmethod
    def test_match_blog_union_id():
        # 测试正则表达式匹配博客文章链接的唯一标识
        # log.debug('invoke method -> test_match_blog_union_id()')
        test_example = test_blog_doc_link
        print(f'test_blog_doc_link: {test_example}')
        # matched = re.search(r'[0-9]{1,}$', test_example, re.M | re.I)
        matched = re.search(test_blog_doc_id_regex, test_example, re.M | re.I)
        if matched:
            print(f'result: {matched.group()}')
            # print(f'union_id: {matched.group("union_id")}')  # union_id
        else:
            print('result: not matched')

    @staticmethod
    def test_match_blog_union_ids():
        # 测试逐个匹配51cto博客测试链接集合,匹配博文的唯一标识
        # log.debug('invoke method -> test_match_blog_union_ids()')
        for link in test_blog_doc_links:
            print(link)
            test_example = test_blog_doc_link
            matched = re.search(test_blog_doc_id_regex, test_example, re.M | re.I)
            print(f'docId = {matched.group()}')


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(TestRegexExpression('test_match_blog_union_id'))  # test_match_blog_union_id
    testunit.addTest(TestRegexExpression('test_match_blog_union_ids'))  # test_match_blog_union_ids
    runner = unittest.TextTestRunner()
    runner.run(testunit)
