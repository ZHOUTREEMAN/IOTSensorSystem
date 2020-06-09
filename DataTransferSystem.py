#!/usr/bin/env python
# encoding: utf-8
import paho.mqtt.client as mqtt
import time
import mysql.connector
# 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
db = mysql.connector.connect(user='root', passwd='123456', database='iotdata',auth_plugin='mysql_native_password')

# 使用cursor()方法获取操作游标
con = db.cursor()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # 在这里处理业务逻辑
    print(msg.topic + " " + msg.payload.decode("utf-8"))
    data0 = msg.topic + " " + msg.payload.decode("utf-8")
    time0=time.strftime("%Y-%m-%d %H:%M:%S")
    con.execute("insert into datamq  (data,time) values ('%s', '%s')" % (data0, time0))
    db.commit()


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("127.0.0.1", 1883, 60)  # ip，端口号，
    client.subscribe("paho/temperature")

    client.loop_forever()