#-*- coding: utf-8 -*
import web
from  setting import *

page_size=20

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

def get_all_article(p, cid):
    start = (p - 1)*page_size
    offset = page_size
    article = db.select('caiji',order='cid desc,post desc,link desc,name desc,date desc',
                        limit="$start,$offset", vars=locals())
    return article	#获取文章


def get_page(p, pages):
    total = db.query("SELECT COUNT(*) AS idpage FROM caiji where page=$pages", vars=locals())[0].idpage
    return page(p, total)	#获取分页数