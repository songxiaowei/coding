#coding=utf-8
import urllib2
import cookielib
#获取Cookie保存到变量
#2016-09-26
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

response = opener.open('http://218.65.107.173/xs_main.aspx?xh=12223323')
for item in cookie:
	print 'Name = '+ item.name
	print 'Value = '+ item.value
