#coding=utf-8
import re
import urllib
#检测p[1]的数据类型
#用type()这个函数检测数据类型
#time:2016-09-21
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getMoney(html):
	reg = r'</span>(.*?)<span class="tag_buy">' 
	context = re.compile(reg)
	p = re.findall(context,html)
	return p


a = getHtml("http://lvhe365.com/")
#print a
b = getMoney(a)
print  b
#print len(b)
print type(b[1])
