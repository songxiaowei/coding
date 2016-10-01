#coding=utf-8
import re
import urllib
import MySQLdb
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def getTitle(html):
	reg = r'<a href=.*? target=.*? title="(.*?)">.*?</a>'
	retitle = re.compile(reg)
	context = re.findall(retitle,html)
	return context
a = getHtml("http://lvhe365.com/")
b = getTitle(a)
'''
i = 0
print b[i]
for i in range(0,len(b)):
	b[i] = "('"+b[i].decode('utf-8')+"')"
'''
print b
'''
conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'villa',
	)
cur = conn.cursor()
#cur.execute("create table money(id varchar(50))")
sqli = "insert into money  values(%s)"
cur.executemany(sqli,b)
cur.close()
conn.commit()
conn.close()
'''
