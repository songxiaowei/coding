#coding=utf-8
import re
import urllib
import MySQLdb
#升级版本
#插入爬取的价格到Mysql中
#2016-09-25
conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'villa',
	)
	
cur = conn.cursor()
#cur.execute('create table money_20160925(id varchar(20))')
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getMoney(html):
	reg = r'</span>(.*?)<span class="tag_buy">' 
	context = re.compile(reg)
	p = re.findall(context,html)
	#for a in p:
	cur.execute("insert into money_20160925 values('songwei')")

#cur.execute("insert into money_20160925 values('songwei')") 	#这里是可以插入数据的

cur.close()
conn.commit()
conn.close()
