#coding=utf-8
import urllib2
import cookielib
#获取Cookie保存到变量
#2016-09-26
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

response = opener.open('http://218.65.107.173/default2.aspx')
for item in cookie:
	print 'Name = '+ item.name
	print 'Value = '+ item.value
	
	
#SyntaxError: Non-ASCII character '\xe8' in file demo2.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
#error问题出现的原因是：没有加utf-8
