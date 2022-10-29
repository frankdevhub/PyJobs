#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：test_bsoup.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/9/4 21:34
"""
import logging as log
import unittest

import requests
from bs4 import BeautifulSoup
from lxml import etree

log.basicConfig(level=log.DEBUG)
test_headers = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
test_51cto_blog_example = "https://blog.51cto.com/oldboy"  # https://blog.51cto.com/oldboy 博客个人空间页面
test_51cto_docs_list_xpath = "//div[@class='common-article-list']"  # //div[@class="common-article-list"] 博客个人空间页面下当前页下的文档对象集合
test_51cto_pagination_tags_xpath = "//ul[@class='pagination']/li/a"  # //ul[@class='pagination']/li/a 博客个人空间当前页页脚分页控件对象


class TestBeautifulSoup(unittest.TestCase):

    @staticmethod
    def test_local():
        # 测试本地运行环境
        log.debug('invoke method -> test_local()')
        html = """
          <html><head><title>The Dormouse's story</title></head>
          <body>
          <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
          <p class="story">Once upon a time there were three little sisters; and their names were
          <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
          <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
          <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
          and they lived at the bottom of a well.</p>
          <p class="story">...</p>
          """
        soup = BeautifulSoup(html)
        assert soup is not None, 'soup cannot be none'
        # soup = BeautifulSoup(open('index.html'))  # 使用本地文件创建对象
        # log.debug(soup.prettify())

    @staticmethod
    def test_51cto_blog_etree() -> etree:
        # 测试抓取博客网页文本html原始内容
        log.debug('invoke method -> test_51cto_blog_etree()')
        response = requests.get(url=test_51cto_blog_example, headers=test_headers)
        page_context = response.text
        # print(page_context)

        tree = etree.HTML(page_context)
        assert tree is not None, 'xml tree cannot be none'
        print(type(tree))
        return tree

    @staticmethod
    def test_51cto_get_page_docs():
        # 测试抓取博客网页对象中的博文简介列表对象
        log.debug('invoke method -> test_51cto_get_page_docs()')
        docs_xpath = test_51cto_docs_list_xpath
        print(f'using xpath = {str(docs_xpath)}')
        # docs_tree = test_51cto_blog_example()
        response = requests.get(url=test_51cto_blog_example, headers=test_headers)
        page_context = response.text
        docs_tree = etree.HTML(page_context)

        assert docs_tree is not None, 'xml tree cannot be none'
        page_docs = docs_tree.xpath(docs_xpath)
        assert page_docs is not None, 'page_docs cannot be none'
        print(f'page_docs size = {len(page_docs)}')
        return

    @staticmethod
    def test_51cto_get_pagination_tags():
        # 测试依据Xpath表达式捕获页脚分页标签对象
        log.debug('invoke method -> test_51cto_get_pagination_tags()')
        page_tree = TestBeautifulSoup.test_51cto_blog_etree()
        assert page_tree is not None, 'page_tree cannot be none'

        # 获取分页控件对象集合
        pagination_tags = page_tree.xpath(test_51cto_pagination_tags_xpath)
        assert pagination_tags is not None, 'pagination_tags cannot be none'
        print(f'pagination_tags size = {len(pagination_tags)}')

        # 遍历分页标签对象集合,获取每一个分页标签对象的超链接地址
        for tag in pagination_tags:
            print(tag)
            print(type(tag))
            # get_text()
            # print(f'tag.get_text() = {tag.get_text()}')
            # outerText
            print(f'attribute outerText = {tag.get("outerText")}')
            # outerHTML
            print(f'attribute outerHTML = {tag.get("outerHTML")}')
            # data-page
            print(f'attribute data-page = {tag.get("data-page")}')
            # href
            print(f'attribute href = {tag.get("href")}')


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    # test_suite.addTest(TestBeautifulSoup('test_local'))  # test_local
    # test_suite.addTest(TestBeautifulSoup('test_51cto_blog_etree'))  # test_51cto_blog_etree
    # test_suite.addTest(TestBeautifulSoup('test_51cto_get_page_docs'))  # test_51cto_get_page_docs
    test_suite.addTest(TestBeautifulSoup('test_51cto_get_pagination_tags'))  # test_51cto_get_pagination_tags
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
