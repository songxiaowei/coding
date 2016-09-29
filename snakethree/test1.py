#Filename: test_mysql.py
from mysql_class import MyDb
'''测试开始'''

'''连接数据库[实例化]'''
my_db = MyDb('127.0.0.1', 'python_user','123123')

'''选择数据库'''
my_db.selectDb('test')

'''修改单条信息'''
dictData = {'class' : 'DD', 'name' : 'Pitt.C','subject':'Match_01','score':60}
condition = [{'class': 'DD','name' : 'Tom'},'OR']
print my_db.saveOne('cla_info',dictData,condition)

'''删除信息'''
condition = [{'class':'DD','name':'bd','id':17},'OR']
print my_db.deleteOne('cla_info',condition)

'''获得单条信息'''
fields = ['class','name','score','comment']
condition = {'id':6}
print my_db.fetchOne('cla_info',condition,fields)


'''新增[单条]'''
dictData = {'class': 'DDD','name': 'Pitt', 'subject': 'Match','score':97}
in_id = my_db.addOne('cla_info',dictData)
print 'Successful add data: ID(%d)' % in_id

'''获取总数'''
condition = {'name':'小明'}
print my_db.getCount('cla_info')

'''事务处理'''
my_db.commit()

'''关闭句柄和连接'''
my_db.close()
































