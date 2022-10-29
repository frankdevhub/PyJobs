# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, String, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BlogDocumentBrief(Base):
    __tablename__ = '51cto_blog_docs_brief'
    __table_args__ = {'comment': '51CTO-博客文档列表内容'}

    id = Column(BigInteger, primary_key=True)
    blog_domain = Column(String(255), comment='博客作者空间链接')
    doc_title = Column(String(100), comment='博客文章标题名称')
    doc_brief = Column(String(255), comment='博客文章摘要内容')
    publish_date = Column(String(50), comment='博文发布时间(字符串日期)')
    context = Column(Text, comment='博客文档原文(text)')
    html = Column(Text, comment='博客文档原文(html)')
    old_data = Column(Text, comment='原始数据')
    renew_data = Column(Text, comment='原始数据')
    compare_data = Column(Text, comment='对比修改的差异的数据(具有操作的指向性)')
    remark = Column(String(255), comment='备注信息')
    create_time = Column(DateTime, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')
    ext1 = Column(String(255), comment='扩展字段1')
    ext2 = Column(String(255), comment='扩展字段2')
    ext3 = Column(String(255), comment='文本扩展字段3')
    status = Column(TINYINT, server_default=text("'1'"))
