#coding=utf-8
import random
import urllib
import urllib2
import cookielib


_xh='12223323'
_pw='123456as'
login_url = 'http://218.65.107.173/default2.aspx'
timetable_url = 'http://218.65.107.173/xs_main.aspx?xh=%s'%_xh
student_cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(student_cookie))

data='__VIEWSTATA'+"dDwxOTI3MTM3Mjk0Ozs+QfR6JETFyd62h+toLFFXl+4IoBw="+'&TextBox1='+'12223323'+'&TextBox2='+'123456as'+'&RadioButtonList1='+"Ñ§Éú"+'&Button1='+""
login_request = urllib2.Request(login_url,data,{
			'Host':'218.65.107.173',
			'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language':'en-US,en;q=0.5',
			'Accept_Encoding':'gzip, deflate',
			'Referer':'http://218.65.107.173/default2.aspx',
			'Cookie':'ASP.NET_SessionId=jdnw5a552sdvpd55oify0lqs',
			'Connection':'keep-alive',
			'Upgrade-Insecure-Requests':'1'
})
opener.open(login_request,data)
html = opener.open(timetable_url).read()
with open('c.txt','a+') as fo:
	fo.write(html)
