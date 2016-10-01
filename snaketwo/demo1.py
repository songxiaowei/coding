#coding=utf-8
import re
import urllib
#实现功能：实现爬虫写入文本这个功能
#技能：遍历数组
#拓展功能：单个字段，应该拓展到多个字段
#time = 2016-09-21
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getMoney(html):
	reg = r'<a href=".*?" target=".*?" title="(.*?)">.*?</a>'
	context = re.compile(reg)
	p = re.findall(context,html)
	i=0
	'''
	with open('a.txt','a+') as fo:
		for i in range(0,len(p)):
			fo.write(p[i])  #字段写入文档，没有分隔，很难看，所以想加个分隔的功能
	'''
	'''
	with open('b.txt','a+') as fo:
		for i in range(0,len(p)):
				fo.write(p[i])
				fo.write("/n") #第一次写的这个发现，不行，还以为错啦，原来是反斜杆的原因（对比下面那段代码）
	'''
	with open('c.txt','a+') as fo:
		for i in range(0,len(p)):
				fo.write(p[i])
				fo.write("\n")


a = getHtml("http://lvhe365.com/")
b = getMoney(a)
print  b
