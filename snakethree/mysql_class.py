#Filename:mysql_class.py
import MySQLdb

class MyDb:
	'''初始化[类似于构造函数]'''
	def __init__(self,host,user,password,charset='utf8'):
		self.host = host
		self.user = user
		self.password = password
		self.charset = charset
		try:
			self.conn = MySQLdb.connect(host = self.host,user = self.user,passwd = self.password,charset = self.charset)
			self.cur = self.conn.cursor()
		except MySQLdb.Error as e:
			print('MySQL Error %d: %s')
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
