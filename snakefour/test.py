#coding=utf-8
#模拟登录教务系统，分析包
import requests
import re
import urllib2
import urllib
import os
while True:
	name = '1223323'
	password = '123456as'
	Target = 'http://218.65.107.173/default2.aspx'
	data = {'__VIEWSTATA':"dDwxOTI3MTM3Mjk0Ozs+QfR6JETFyd62h+toLFFXl+4IoBw=",'TextBox1':str(name),'TextBox2':str(password),
	'RadioButtonList1':"Ñ§Éú",'Button1':""}
	s=requests.session()
	r = s.post(Target,data)
	html = urllib.urlopen('http://218.65.107.173/xs_main.aspx?xh=12223323')
	page = html.read()
	print page
