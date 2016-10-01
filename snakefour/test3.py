#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import os
import getpass

def getName(loginPage):
	Sname = r'<span id="xhxm">(.+)同学</span>'
	Sname = re.compile(Sname)
	try:
		return Sname.findall(loginPage)[0]
	except IndexError, e:
		raise e
		print "Uer-name or password error,try agin!"
		main()
	
def main():
	loginURL = 'http://218.65.107.173/default2.aspx'
	page = urllib2.urlopen(loginURL).read()
	postdata = urllib.urlencode({
		'__VIEWSTATA':"dDwxOTI3MTM3Mjk0Ozs+QfR6JETFyd62h+toLFFXl+4IoBw=",
		'TextBox1':'12223323',
		'TextBox2':'123456as',
		'RadioButtonList1':"Ñ§Éú",
		'Button1':""
	})
	
	headers = {
			'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
	}
	
	cookie = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	myRequest = urllib2.Request(loginURL,postdata,headers)
	loginPage = opener.open(myRequest).read()
	page = unicode(loginPage,'gb2312').encode("utf-8")
	
	try:
		name = getName(page)
	except IndexError, e:
		print "User-name or password error, try again!"
		main()
		exit()
	else:
		pass
		
	head = {
			'Host':'218.65.107.173',
			'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language':'en-US,en;q=0.5',
			'Accept_Encoding':'gzip, deflate',
			'Referer':'http://218.65.107.173/default2.aspx',
			'Cookie':'ASP.NET_SessionId=jdnw5a552sdvpd55oify0lqs',
			'Connection':'keep-alive',
			'Upgrade-Insecure-Requests':'1'
	}
	
	MyRequest = urllib2.Request('http://218.65.107.173/xs_main.aspx?xh=12223323',None,head)
	loginPage = unicode(opener.open(MyRequest).read(),'gb2312').encode("utf-8")
	
if __name__ == '__main__':
		main()
