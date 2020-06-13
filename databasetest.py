import MySQLdb
import time
# 云端数据库测试代码
# 打开数据库连接
db = MySQLdb.connect("62.234.154.66", "root", "123456", "internetofthings", charset='utf8' )
# 使用cursor()方法获取操作游标
con = db.cursor()
con.execute("insert into computer values ('11','1','2020-6-13 08:00:00','1','30','50','80')")
con.execute("insert into temperature values ('16','2020-6-13 00:00:00','37.0','1','1')")
con.execute("insert into people values ('11','2020-6-13 08:00:00','8','1')")
con.execute("insert into humidity values ('21','2020-6-1-13 00:00:03','88','1')")
db.commit()