#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File ：sqlalchemy_orm.py
@Author ：frankdevhub@gmail.com
@Blog : http://blog.frankdevhub.site
@Date ：2021/3/7 22:23
"""

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

def get_session():
    engine = db.create_engine('mysql+pymysql://root:Fxmf7fa@0806@127.0.0.1:3306/blog_documents')
    assert engine is not None, f'variable engine cannot be none'
    session_maker = sessionmaker(bind=engine)
    assert session_maker is not None, f'variable session_maker cannot be none'
    return session_maker
