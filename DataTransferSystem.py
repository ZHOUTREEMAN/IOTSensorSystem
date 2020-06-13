#!/usr/bin/env python
# encoding: utf-8
import paho.mqtt.client as mqtt
import time
import MySQLdb
import mysql.connector
# 打开云端数据库连接
db = MySQLdb.connect("62.234.154.66", "root", "123456", "internetofthings", charset='utf8' )

# 使用cursor()方法获取操作游标
con = db.cursor()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # 在这里处理业务逻辑
    topic = msg.topic
    data0 = msg.payload.decode("utf-8")
    # 对电脑信息数据处理
    if topic == "computer":
        con.execute("insert into computer  (computer_id,time,state,cpu,memory,disk) values (%s)" % data0)
        print("转存主机传感器数据")
    # 对温度数据处理
    if topic == "temperature":
        con.execute("insert into temperature  (time,temperature,computer_id,room_id) values (%s)" % data0)
        print("转存温度传感器数据")
    # 对湿度数据处理
    if topic == "humidity":
        con.execute("insert into humidity  (time,humidity,room_id) values (%s)" % data0)
        print("转存湿度传感器数据")
    # 对人员数量数据处理
    if topic == "people":
        con.execute("insert into people  (time,number_of_people,room_id) values (%s)" % data0)
        print("转存门禁传感器数据")
    # con.execute("insert into datamq  (data,time) values ('%s', '%s')" % (data0, time0))
    db.commit()


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("127.0.0.1", 1883, 60)  # ip，端口号，
    client.subscribe("computer")
    client.subscribe("temperature")
    client.subscribe("humidity")
    client.subscribe("people")
    client.loop_forever()