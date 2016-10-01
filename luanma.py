#coding=utf-8
import re
import urllib
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
'''i=0
for i in range(0,len(b)):
'''	
print b[2]
print b[2].decode("utf-8")

i=0
for i in range(0,3):
	b[i] = b[i].decode("utf-8")
	print b[i]

