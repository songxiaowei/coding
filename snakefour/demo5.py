#coding=utf-8
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookie.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
	'uesr':'12223323',
	'passw':'123456as',
})

loginUrl = 'http://218.65.107.173/default2.aspx'
result = opnener.open(loginurl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeUrl = 'http://218.65.107.173/xs_main.aspx?xh=12223323'

result = opener.open(gradeUrl)
print result.read()

#模拟登录失败
