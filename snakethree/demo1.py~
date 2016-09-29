#coding=utf-8
import MySQLdb
#作用：连接数据库并插入一个数
#2016-9-25
conn=MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'villa',
	)
cur = conn.cursor()

#创建数据表
cur.execute("create table teacher(id int)")

#插入一条数据
cur.execute("insert into teacher values('2')")

cur.close()
conn.commit()
conn.close()
