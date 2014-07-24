#-*- coding: utf-8 -*
import requests
from pyquery import PyQuery as pq
from db import *
import time

class Ershou_game:
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
            times_a = tr('td[class="by"] span').text()
            times=time.strftime("%Y-%m-%d",time.strptime(times_a,"%Y-%m-%d"))
            # times = tr('td em').eq(1).text()
            pages = 'page'
            Piliang = [title,link,nname,times,pages,tagess]
            #写入指定的表
            LjDB.execute("insert into caiji(post,link,name,date,page,tag) values (?,?,?,?,?,?)",Piliang)
            conn.commit()
            #删除重复数据
            LjDB.execute("delete from caiji where link  in (select  link  from caiji  group  by  link   having  count(link) > 1) and rowid not in (select min(rowid) from  caiji  group by link  having count(link )>1)")
            # print("post:%s link: %s %r %r" %(title,link,nname,times))

####

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
            LjDB.execute("insert into caiji(post,link,name,date,page,tag) values (?,?,?,?,?,?)",Piliang)
            conn.commit()
            LjDB.execute("delete from caiji where link  in (select  link  from caiji  group  by  link   having  count(link) > 1) and rowid not in (select min(rowid) from  caiji  group by link  having count(link )>1)")

class Ershou_mydigit:
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
        self.page(Caiji_open.content.decode('gbk','ignore'))

    def page(self,Lianjie):
        dom = pq(Lianjie)
        tag_tbdoy = dom('tbody[id="threadlist"] tr[class="tr3"]')
        tag_tbdoy.each(lambda index,code: self.getContent(index,code))

    def getContent(self,index,node):
        tr = pq(node)
        if (tr('td a').eq(1)):
            title = tr('td[class="subject"] a').eq(1).text()
            link = self.get_host + tr('td a').eq(2).attr.href
            nname = self.wname
            tagess = self.ntage
            times_a = tr('td p').eq(0).text()
            times = time.strftime("%Y-%m-%d",time.strptime(times_a,"%Y-%m-%d"))
            pages = 'page'
            Piliang = [title,link,nname,times,pages,tagess]
            LjDB.execute("insert into caiji(post,link,name,date,page,tag) values (?,?,?,?,?,?)",Piliang)
            conn.commit()
            LjDB.execute("delete from caiji where link  in (select  link  from caiji  group  by  link   having  count(link) > 1) and rowid not in (select min(rowid) from  caiji  group by link  having count(link )>1)")
