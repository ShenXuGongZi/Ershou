#-*- coding: utf-8 -*
import web
from  setting import *

page_size=15

def page(p=1, total=1):
    Page = []
    if (total < page_size):
        page_count = 1
    elif (total % page_size):
        page_count = total / page_size + 1
    else:
        page_count = total / page_size

    if p > page_count:
        return Page

    if page_count != 1:
        def link(l):
            Page.append('<a href="' + str(l) + '">' + str(l) + '</a>')

        if p != 1:
            Page.append('<a href="' + str(p - 1) + '">' + u'<上一页' + '</a>')
        if p > 11:
            for i in range(p - 10, p):
                link(i)
        else:
            for i in range(1, p):
                link(i)

        Page.append('<a href="' + str(p) + '"><b>' + str(p) + '</b></a>')

        if p + 10 <= page_count:
            for i in range(p + 1, p + 11):
                link(i)
        else:
            pass
            for i in range(p + 1, page_count + 1):
                link(i)

        if p != page_count:
            Page.append('<a href="' + str(p + 1) + '">' + u'下一页>' + '</a>')
    return Page
#查询数据库获取文章
def get_all_article(p, cid):
    start = (p - 1)*page_size
    offset = page_size
    article = db.select('caiji',order='date desc,link desc,cid desc,post desc,name desc,tag',
                        limit="$start,$offset", vars=locals())
    return article	#获取文章

#获取分页，遍历page标签得到总数据量
def get_page(p, pages):
    total = db.query("SELECT COUNT(*) AS idpage FROM caiji where page=$pages", vars=locals())[0].idpage
    return page(p, total)	#获取分页数


#tag分类获取
def get_all_tag(p, tags):
    start = (p - 1)*page_size
    offset = page_size
    tag = db.select('caiji',where="tag=$tags",order='date desc,cid desc,post desc,link desc,name desc,tag desc',
                        limit="$start,$offset", vars=locals())
    return tag	#获取文章
#
def get_tag(p, tags):
    total = db.query("SELECT COUNT(*) AS idtag FROM caiji where tag=$tags", vars=locals())[0].idtag
    return page(p, total)	#获取分页数




#首页函数
#定义数据库
# def dbhook():
#     '''数据库的hook'''
#     def _(func):
#         '''_'''
#         def wrapper(*a, **kw):
#             '''wrapper'''
#             _handler = a[0]
#             db = "/home/hang/文档/PythonEX/Ershou/DB/ershou.db"
#             _handler.conn = sqlite3.connect(db,check_same_thread = False)
#             _handler.conn.execute('pragma foreign_keys = on')
#             _handler.conn.commit()
#             _handler.cur = _handler.conn.cursor()
#             try:
#                 result = func(*a, **kw)
#             finally:
#                 _handler.conn.close()
#             return result
#         return wrapper
#     return _
