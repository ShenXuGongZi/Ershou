# -*-coding:utf-8 -*
import web
from web import storage
import model
from tpl import render_home as render
from setting import *

j = storage()

class index:
    def GET(self):
        referer = web.ctx.env.get('HTTP_REFERER', '/index/page/1')
        raise web.seeother(referer)
#主页数据
class news:
    def GET(self, p='10'):
        p = int(p)
        j.article = model.get_all_article(p, cid=90)
        j.page = model.get_page(p, pages='page')
        return render('news',
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      **j)

class tag:
    def GET(self, p='10'):
        p = int(p)
        j.article = model.get_all_tag(p, tags='DianWan')
        j.page = model.get_tag(p, tags='DianWan')
        return render('tag',
                      title=webname,
                      gonggao_h=Gonggao_S,
                      footer=dibu,
                      info=fubiaoti,
                      homelink=weblink,
                      game=dwgame,
                      **j)



