#coding=utf-8

import MySQLdb
#升级版本
#插入一组数
#2016-09-25
conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'villa',
	)
	
cur = conn.cursor()

for p in [1,2,3,4,5]:
	cur.execute("insert into student values('%s')" % (p))

cur.close()
conn.commit()
conn.close()
