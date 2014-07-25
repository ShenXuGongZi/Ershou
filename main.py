# -*-coding:utf-8 -*
import web
from web import storage
import model
from tpl import render_home as render
from setting import *
import sys

#解决中文问题
reload(sys)
sys.setdefaultencoding('utf8')

j = storage()


# class index(object):
#     def GET(self):
#         web.HTTPError('301',{'Location':'/index/page/1'})

#主页数据
class page:
    def GET(self, p='10'):
        p = int(p)
        j.article = model.get_all_article(p, cid=90)
        j.page = model.get_page(p, pages='page')
        return render('page',
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      shuma=dwshuma,
                      weifeng=weifengs,
                      **j)

class game:
    def GET(self, p='10'):
        p = int(p)
        j.article = model.get_all_tag(p, tags='dianwanbashi')
        j.page = model.get_tag(p, tags='dianwanbashi')
        return render('game',
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      shuma=dwshuma,
                      weifeng=weifengs,
                      **j)

class shuma:
    def GET(self, p='10'):
        p = int(p)
        j.article = model.get_all_tag(p, tags='shumazhijia')
        j.page = model.get_tag(p, tags='shumazhijia')
        return render('shuma',
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      shuma=dwshuma,
                      weifeng=weifengs,
                      **j)

class weifeng:
    def GET(self, p='10'):
        p = int(p)
        j.article = model.get_all_tag(p, tags='weifeng')
        j.page = model.get_tag(p, tags='weifeng')
        return render('weifeng',
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      shuma=dwshuma,
                      weifeng=weifengs,
                      **j)


# class search:
#     def GET(self):
#         conn = sqlite3.connect('./DB/ershou.db')
#         LjDB = conn.cursor()
#         searcher = web.input()
#         DBsearch = LjDB.execute("select * from caiji where post like ?",
#                             ('%{}%'.format(searcher),))
#         return render('search',
#                       title=webname,
#                       gonggao_h=Gonggao_S,
#                       footer=dibu,
#                       info=fubiaoti,
#                       homelink=weblink,
#                       game=dwgame,
#                       shuma=dwshuma,
#                       searchs=DBsearch,
#                       heardserch=searcher
#                       )

#搜索实验
class search(object):
    def GET(self):
        conn = sqlite3.connect('./DB/ershou.db')
        #解决数据库不能查询中文问题
        conn.text_factory = str
        LjDB = conn.cursor()
        i = web.input(name=None)
        c = LjDB.execute("select * from caiji where post like ?",
                            ('%{}%'.format(i.name),))
        # return "Listing info about user:{0} ".i.name
        return render('search',
                      searchs=c,
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      shuma=dwshuma,
                      weifeng=weifengs,)


