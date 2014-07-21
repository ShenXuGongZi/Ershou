#-*- coding: utf-8 -*
import web
import sqlite3
from web.contrib.template import  render_jinja


# db = web.database(dbn='sqlite',db='/home/hang/文档/PythonEX/Ershou/DB/ershou.db')

#title跟LOGO位置
webname = u'喵喵的二手站'
#公告区域
Gonggao_S = u'小站才开张请扩散喵！'
#底部
dibu = u'2014. 肾虚公子 本站基于Python制作.'
#副标题
fubiaoti = u'{这是二手集合网站} 喵傲~~'

#定义数据库
def dbhook():
    '''数据库的hook'''
    def _(func):
        '''_'''
        def wrapper(*a, **kw):
            '''wrapper'''
            _handler = a[0]
            db = "/home/hang/文档/PythonEX/Ershou/DB/ershou.db"
            _handler.conn = sqlite3.connect(db,check_same_thread = False)
            _handler.conn.execute('pragma foreign_keys = on')
            _handler.conn.commit()
            _handler.cur = _handler.conn.cursor()
            try:
                result = func(*a, **kw)
            finally:
                _handler.conn.close()
            return result
        return wrapper
    return _

#定义模板路径 jinja2
render = render_jinja(
        'templates',   # 设置模板路径.
        encoding = 'utf-8', # 编码.
    )

#定义模板各种变量
class index:
    @dbhook()
    def GET(self):
        #读取数据库，并只显示数据库前6行  倒序读取 order by id desc 倒序读取 id这个值
        DBshuC = self.cur.execute("SELECT post,link,name,date from caiji order by id desc LIMIT 20")
        self.conn.commit()
        # i = web.input(name=None)
        return  render.demo(
            title=webname,
            gonggao_h=Gonggao_S,
            footer=dibu,
            info=fubiaoti,
            posts=DBshuC,
            )

