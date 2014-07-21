#-*- coding: utf-8 -*
import web
import sqlite3
from web.contrib.template import  render_jinja

conn = sqlite3.connect('/home/hang/文档/PythonEX/Ershou/DB/ershou.db')
ChaX = conn.cursor()
conn.commit()
#title跟LOGO位置
webname = u'喵喵的二手站'
#公告区域
Gonggao_S = u'小站才开张请扩散喵！'
#底部
dibu = u'2014. 肾虚公子 本站基于Python制作.'
#副标题
fubiaoti = u'{这是二手集合网站} 喵傲~~'
###数据库读取
#查询数据库caiji表，并获取信息
DBShuC = ChaX.execute("SELECT post,link,name,date from caiji")
#写入循环
for row in DBShuC:
    #查询caiji表第一个标签,post
    Bioti = row[0]
    #查询caiji表 link标签
    Lianj = row[1]
    Laiy = row[2]
    Shijian = row[3]


# print col_name_list
conn.close()

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

render = render_jinja(
        'templates',   # 设置模板路径.
        encoding = 'utf-8', # 编码.
    )

class index:
    def GET(self):
        # i = web.input(name=None)
        return  render.demo(
            title=webname,
            gonggao_h=Gonggao_S,
            footer=dibu,
            info=fubiaoti,
            link=Lianj,
            post=Bioti,
            name=Laiy,
            time=Shijian)

# print render.demo()