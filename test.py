# #-*- coding: utf-8 -*
# import web
# from web import storage
# #链接数据库文件
# db = web.database(dbn='sqlite',db='./DB/ershous.db')
#
#
# # j = storage()
# # #标签查找 查找caiji表内name标签下所有有TGbus的值
# # myvar = dict(post="TGbus")
# # for row in db.select('caiji', myvar, where="name = $post"):
# #     print row
#
#
#
#
# #
# # myvar = dict(cid="10")
# # for results in db.select('caiji',myvar,where="id=$cid"):
# #     print results
#
# cid='10'
# total = db.query("select count(*) as count from caiji")[0]
# print total


#-*- coding: utf-8 -*
import requests
from pyquery import PyQuery as pq
import time
import sqlite3

class Ershou:
    def __init__(self,url,host,webname,tage):
        self.Caiji_UA = {
        'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
        'Accept-Language:':'zh-CN,zh;q=0.8',
        'Referer': host,
        'Content-Type': 'text/xml; charset=utf-8'
        }
        self.host = url
        self.get_host = host
        self.wname = webname
        self.ntage = tage
        Caiji_open = requests.get( self.host, headers = self.Caiji_UA )
        self.page(Caiji_open.content.decode('utf-8','ignore'))
    def page(self,Lianjie):
        dom = pq(Lianjie)
        tag_tbdoy = dom('tbody tr')
        tag_tbdoy.each(lambda index,code: self.getContent(index,code))
    def getContent(self,index,node):
        tr = pq(node)
        if (tr('td a').eq(1)):
            title = tr('th a').eq(1).text()
            link = self.get_host + tr('th a').eq(1).attr.href
            nname = self.wname
            tagess = self.ntage
            times_a = tr('span  span').attr.title
            times=time.strftime("%Y-%m-%d",time.strptime(times_a,"%Y-%m-%d"))
            pages = 'page'
            Piliang = [title,link,nname,times,pages,tagess]
            print Piliang

# if __name__ == '__main__':
# Ershou("http://bbs.tgbus.com/forum-50-2.html",'http://bbs.tgbus.com/','TGbus','DianWan')
# Ershou("http://bbs.mydigit.cn/thread.php?fid=73&page=2",'http://bbs.mydigit.cn/','mydigit','Shuma')
# Ershou('http://bbs.feng.com/forum.php?mod=forumdisplay&fid=29&page=2','http://bbs.feng.com/','WeiFeng','Shuma')


# conn = sqlite3.connect('./DB/ershou.db')
# # #使数据库可以录入中文
# # conn.text_factory = str
# LjDB = conn.cursor()
# name = raw_input('search:')
# DBsearch = LjDB.execute("select * from caiji where post like ?",
#                             ('%{}%'.format(name),))
# for ss in DBsearch:
#     print ss[1],
#     print ss[2]
#
# ss = LjDB.execute('delete from caiji where link  in (select  link  from caiji  group  by  link   having  count(link) > 1)and rowid not in (select min(rowid) from  caiji  group by link  having count(link )>1)')
# print ss


# rr = '2014-6-23'
# ss = time.strftime("%Y-%m-%d",time.strptime(rr,"%Y-%m-%d"))
# print ss

from random import choice

suiji = dict(a=1, c=5)
suiji2 = suiji[choice(suiji.keys())]

print suiji2



# select * from caiji where post like '%iphone5%'

