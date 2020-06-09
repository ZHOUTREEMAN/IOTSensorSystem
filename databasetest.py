import mysql.connector
import time
# 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
db = mysql.connector.connect(user='root', passwd='123456', database='iotdata',auth_plugin='mysql_native_password')
# 使用cursor()方法获取操作游标
con = db.cursor()
time0 = time.time()
timestr=time.strftime("%Y-%m-%d %H:%M:%S")
print(timestr)
data0="paho/temperature b this is message:1374 "
print('2019-01-01')
con.execute("insert into datamq (data,time) values ('%s', '%s')" % (data0, timestr))
db.commit()