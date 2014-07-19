#encoding: utf-8
import requests
from pyquery import PyQuery as pq
 
agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
content_type = "applicationself.s.xsrf/x-www-form-urlencoded; charset=UTF-8"
 
class Sjtu:
    def __init__(self,url,host):
        self.host = url
        self.main_host = host
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': agent})
        self.s.headers.update({'Referer': self.host })
        self.s.headers.update({'Content-Type': content_type })
        r = self.s.get( self.host, headers = self.s.headers )
        self.page(r.content.decode( 'utf-8','ignore'))
    
    def page(self,content):
        dom = pq(content)
        tag_li = dom('tbody tr')
        tag_li.each(lambda index,code: self.getContent(index,code))
            
    def getContent(self, index, node):
        li = pq(node)
        if (li("td a").eq(1)):
                 title =  li("th a").eq(1).text()
                 link  =  self.main_host + li("th a").eq(1).attr.href
                 print("post: %s and %s" % (title, link))
    
if __name__ == "__main__":
    print '='*30 + 'TGbus' + '='*30
    Sjtu("http://bbs.tgbus.com/forum-50-1.html",'http://bbs.tgbus.com/')
    print '='*30 + 'WeiFeng' + '='*30
    Sjtu('http://bbs.feng.com/thread-htm-fid-29.html','http://bbs.feng.com/')
#s
#r