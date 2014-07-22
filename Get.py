#-*- coding: utf-8 -*
import requests
from pyquery import PyQuery as pq
import time
import sqlite3

conn = sqlite3.connect('/home/hang/文档/PythonEX/Ershou/DB/ershou.db')
#使数据库可以录入中文
conn.text_factory = str
LjDB = conn.cursor()
#创建数据库 并设置自增长id INTEGER PRIMARY KEY
# LjDB.execute('''create table caiji (cid INTEGER PRIMARY KEY,post text, link text, name text,date text,page text,tag text)''')

class Ershou:
    def __init__(self,url,host,webname,tage):
        #定义UA
        self.Caiji_UA = {
        'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
        'Accept-Language:':'zh-CN,zh;q=0.8',
        'Referer': host,
        'Content-Type': 'text/xml; charset=utf-8'
        }
        #设置域名变量
        self.host = url
        #设置URL显示变量
        self.get_host = host
        #网站名称
        self.wname = webname
        self.ntage = tage
        #模拟浏览器打开网站
        Caiji_open = requests.get( self.host, headers = self.Caiji_UA )
        #设置字符给page
        self.page(Caiji_open.content.decode('utf-8','ignore'))
    #设置页面采集函数
    def page(self,Lianjie):
        #这只pq抓取网页
        dom = pq(Lianjie)
        #抓取网页tbody tr 两个标签
        tag_tbdoy = dom('tbody tr')
        #对每一个元素进行操作
        tag_tbdoy.each(lambda index,code: self.getContent(index,code))
    #抓取页面内标签
    def getContent(self,index,node):
        #设置抓取标签
        tr = pq(node)
        #永真，用pq拉取td a标签 //eq返回被检索的元素
        if (tr('td a').eq(1)):
            title = tr('th a').eq(1).text()
            link = self.get_host + tr('th a').eq(1).attr.href
            #网站名
            nname = self.wname
            #标签
            tagess = self.ntage
            #时间
            # times = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            # times = tr('td[class="by"] em').eq(1).text()
            times = tr('span').eq(1).text()
            pages = 'page'
            Piliang = [title,link,nname,times,pages,tagess]
            #写入指定的表
            LjDB.execute("insert into caiji(post,link,name,date,page,tag) values (?,?,?,?,?,?)",Piliang)
            conn.commit()
            # print("post:%s link: %s %r %r" %(title,link,nname,times))

#if __name__ == '__main__':
Ershou("http://bbs.tgbus.com/forum-50-2.html",'http://bbs.tgbus.com/','电玩巴士','DianWan')
Ershou('http://bbs.feng.com/forum.php?mod=forumdisplay&fid=29&page=2','http://bbs.feng.com/','威锋','Shuma')
Ershou('http://www.chiphell.com/forum-97-2.html','http://www.chiphell.com/','chiphell','Shuma')
# 关闭数据库
conn.close()