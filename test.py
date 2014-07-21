#-*- coding: utf-8 -*
import sqlite3

#链接数据库文件
#如果数据库文件不存在，回新建一个，如果存在则打开此文件
conn = sqlite3.connect('DB/ershou.db')

c = conn.cursor()

#创建表格
#c.execute('''create table caiji (post text, link text, name text,  date text)''')

# 插入数据，执行SQL语句
# c.execute("""insert into caiji
#           values ('【和田玉】几个平安扣和平安环 打包出了 有好几个 只要500','http://bbs.feng.com/read-htm-tid-5099560.html','WeoFemg','2014-07-21')""")

#将变动保存到数据库文件，如果没有执行词语句，则前面的insert 语句操作不会被保存
conn.commit()

#查询数据库caiji表，并获取信息
rec = c.execute("SELECT post,link,name,date from caiji")
def test():
    for row in rec:
        #查询caiji表第一个标签,post
        Bioti = row[0]
        #查询caiji表 link标签
        Lianj = row[1]
        Laiy = row[2]
        Shijian = row[3]
        x=0
        # rr = u'<tr><td><a href="%r" target="_blank">%r</a></td><td>%r</td><td>%r</td></tr>'%(Lianj,Bioti,Laiy,Shijian)
        # rr+=1
        print Bioti
        print Lianj
        print Laiy
        print Shijian

yy = test()









#ss = row[0]


# def tr():
#     for test in row:
#             print u'<tr>'
#             print u'<td><a href="%r" target="_blank">%r</a></td>'%(Lianj,Bioti)
#             print u'<td>%r</td>'%Laiy
#             print u'<td>%r</td>'%Shijian
#
# print tr()



#写入循环
# for row in rec:
#     #查询caiji表第一个标签,post
#     print row[0],
#     #查询caiji表 link标签
#     print row[1],
#     print row[2],
#     print row[3]


# print col_name_list
conn.close()