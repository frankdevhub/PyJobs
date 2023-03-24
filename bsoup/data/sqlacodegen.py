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
    cmd = "sqlacodegen  mysql+pymysql://root:root@admin6@localhost:3306/jobs --outfile sqlacodegen_models.py"
    os.system(cmd)
