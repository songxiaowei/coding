#coding=utf-8
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

hosturl = 'http://218.65.107.173/default2.aspx'

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)

headers = {
	'Host':'218.65.107.173',
	'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate',
	'Referer':'http://218.65.107.173/default2.aspx',
	'Cookie':'ASP.NET_SessionId=rrthlifcyijb2m45vtdy5h55',
	'Connection':'keep-alive',
	'Upgrade-Insecure-Requests':'1',
	}

postData = {
	'_VIEWSTATE':'dDwxOTI3MTM3Mjk0Ozs+QfR6JETFyd62h+toLFFXl+4IoBw=',
	'TextBox1':'12223323',
	'TextBox2':'123456as',
	'RadioButtonList1':"123321321",
	'Button1':"",
	}
	
postData = urllib.urlencode(postData)

request = urllib2.Request(hosturl,postData,headers)
print request
response = urllib2.urlopen(request)
text = resopnse.read()
print text
