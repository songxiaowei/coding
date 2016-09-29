#coding=utf-8
import re
import urllib
#验证demo1所做的测试文档
#问题：这个有爬取中文信息有乱码问题
#2016-09-25
'''
测试思路：
1 先测试getHtml这个功能能不能成功
2 再对getMoney模块测试，最后确定是正则表达式有问题，因为更改reg里的数据就能成功哦
'''
#time = 2016-09-21
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read() #乱码问题出现'\xe6\x88\x91\xe7\x9a\x84\xe6\x94\xb6\xe8\x97\x8f'
	#html = page.read().decode('UTF-8') #出现u'\u6211\u7684\u6536\u85cf'
	return html

def getMoney(html):
	reg = r'<a href=".*?" target=".*?" title="(.*?)">.*?</a>'
	context = re.compile(reg)
	p = re.findall(context,html)
	return p


a = getHtml("http://lvhe365.com/")
b = getMoney(a)
print  b

'''
def getTitle(html):
	reg = r'<a href=.*? target=.*? title="(.*?)">.*?</a>'
	retitle = re.compile(reg)
	context = re.findall(retitle,html)
	return context
a = getHtml("http://lvhe365.com/")
b = getTitle(a)
'''


