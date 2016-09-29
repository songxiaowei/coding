#coding=utf-8
import re
import urllib
#实现功能：爬取绿禾网的价钱信息，只是单个信息
#拓展：希望能爬取多维度的信息，比如价钱代表的物品也爬取，并对应
#bug的原因是正则表达式写的不正确，导致b输出有问题
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
print len(b)


'''
分析html，其实最好是能缩小范围得写正则表达式，这样爬取的准确率就会高一点，不然很容易出错
<span style="font-size:14px;font-family:微软雅黑;font-weight:bold;">￥
</span>19.90<span class="tag_buy"> <a href="javascript:addToCart(21813,1)">马上抢</a></span>
'''
