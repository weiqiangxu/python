#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="123456",   # 数据库密码
  database="runoob_db" # 数据库名称
)
 

# 创建数据库 
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE runoob_db")

# 创建数据表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


# 数据插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

# 数据表内容有更新，必须使用到该语句
mydb.commit()
 
# 打印结果
print(mycursor.rowcount, "记录插入成功。")


# 批量插入数据
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
 
mycursor.executemany(sql, val)
 
mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")


# 查询所有记录
mycursor.execute("SELECT * FROM sites")
 
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)