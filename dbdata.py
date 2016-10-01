#coding=utf-8
import MySQLdb

conn = MySQLdb.connect(
	host='localhost',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'villa',
	)
cur = conn.cursor()

#插入数据
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
cur.close()
conn.commit()
conn.close()

