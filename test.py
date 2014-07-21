#-*- coding: utf-8 -*
import sqlite3
import web

#链接数据库文件
#如果数据库文件不存在，回新建一个，如果存在则打开此文件
# conn = sqlite3.connect('DB/ershou.db')
db = web.database(dbn='sqlite',db='./DB/ershou.db')

# c = db.cursor()

#创建表格
#c.execute('''create table caiji (Id INTEGER PRIMARY KEY,post text, link text, name text,  date text)''')

# uu = 0
# yy = 1
# uu += yy
# oo = ['title','link','nname','times']
# # 插入数据，执行SQL语句
# c.execute("insert into caiji(post,link,name,date) values (?,?,?,?)",oo)
# conn.commit()
#将变动保存到数据库文件，如果没有执行词语句，则前面的insert 语句操作不会被保存


#查询数据库caiji表，并获取信息
# c.execute("insert into caijis values ('%r','%r','%r','%r')"%())
#rec = c.execute("SELECT post,link,name,date from caiji")
myvar = dict(name="Bob")
for row in db.select('caiji',where="id<10"):
    print row

#db.close()

# "CREATE TABLE IF NOT EXISTS %s(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(40),Flag INTEGER)"% table