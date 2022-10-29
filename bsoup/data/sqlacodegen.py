#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：sqlacodegen.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/10/3 11:55
"""
import logging as log
import os

log.basicConfig(level=log.DEBUG)

if __name__ == '__main__':
    log.debug('init sqlacodegen')
    cmd = "sqlacodegen  mysql+pymysql://root:Fxmf7fa@0806@localhost:3306/blog_documents --outfile sqlacodegen_models.py"
    os.system(cmd)
