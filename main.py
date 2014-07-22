# -*-coding:utf-8 -*
import web
from web import storage
import model
from tpl import render_home as render
from setting import *

j = storage()


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
                      **j)

