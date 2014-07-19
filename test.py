#-*- coding: utf-8 -*
import requests
import urllib
import urllib2
from pyquery import PyQuery as pq

# UA = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
# #
# s = requests.post(url='http://bbs.smartisan.cn/forum.php?mod=forumdisplay&fid=2',headers=UA)
# rr = s.text
# # print (s.url)
# print(s.text)

Caiji_Ua = {
    'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Accept-Encoding:':'gzip,deflate,sdch',
    'Accept-Language:':'zh-CN,zh;q=0.8',
    'Host':'bbs.smartisan.cn'
}
Caiji_open = requests.post(url='http://bbs.smartisan.cn/forum.php?mod=forumdisplay&fid=2',headers=Caiji_Ua)
Caiji_Sc = Caiji_open.text
# Caiji_a = pq(Caiji_Sc)
# # test2 = Caiji_a("th a").eq(1).attr.href
# test = Caiji_a('a[class="s xst"]').text()
# #print test
# # print test2
# for ceshi in test:
#     print ceshi
li = pq(Caiji_Sc)
if (li("th a").eq(1)):
         title =  li('a[class="s xst"]').eq(1).text()
         link  =  'http://bbs.smartisan.cn/'+li("th a").eq(1).attr.href
         print("post: %s and %s" % (title, link))