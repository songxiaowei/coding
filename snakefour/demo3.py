#coding=utf-8
import cookielib
import urllib2
#保存Cookie到文件
#2016-09-26
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://218.65.107.173/default2.aspx")
cookie.save(ignore_discard=True,ignore_expires=True)
