#-*- coding: utf-8 -*
import sqlite3

conn = sqlite3.connect('/home/hang/文档/PythonEX/Ershou/DB/ershou.db')
#使数据库可以录入中文
conn.text_factory = str
LjDB = conn.cursor()
#创建数据库 并设置自增长id INTEGER PRIMARY KEY
# LjDB.execute('''create table caiji (cid INTEGER PRIMARY KEY,post text, link text, name text,date key,page text,tag text)''')