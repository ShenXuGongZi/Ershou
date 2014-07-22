#-*- coding: utf-8 -*
import web
from web import storage
#链接数据库文件
db = web.database(dbn='sqlite',db='./DB/ershous.db')


# j = storage()
# #标签查找 查找caiji表内name标签下所有有TGbus的值
# myvar = dict(post="TGbus")
# for row in db.select('caiji', myvar, where="name = $post"):
#     print row




#
# myvar = dict(cid="10")
# for results in db.select('caiji',myvar,where="id=$cid"):
#     print results

cid='10'
total = db.query("select count(*) as count from caiji")[0]
print total