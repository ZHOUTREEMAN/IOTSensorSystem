# encoding: utf-8
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import random

idx = 0  # 往paho/temperature 一直发送内容
while True:
    print("send success")
    # 传感器数据模拟：
    # 计算机的传感器数据：
    for i in range(72):
        computerId = i+1
        time0 = time.strftime("%Y-%m-%d %H:%M:%S")
        # 计算机运行状态
        state = random.randint(0, 1)
        cpu = random.uniform(0, 100)
        memory = random.uniform(0, 100)
        disk = random.uniform(0, 100)
        # 整合信息
        info = "'"+str(computerId) + "','" + str(time0)+ "','"  + str(state) + "','" + str(cpu)+ "','" +str(memory)+ "','" +str(disk)+"'"
        # 发送数据到mqtt服务器
        publish.single("computer",
                       payload="%s" % info,  # 传送内容
                       hostname="127.0.0.1",  # 你的ip地址
                       client_id="lora1",
                       port=1883,
                       protocol=mqtt.MQTTv311)
         # 计算机温度
        temperature_computer= random.uniform(10, 99)
         # 整合信息
        info = "'" + str(time0) + "','" + str(temperature_computer) + "','" + str(computerId) + "','0'"
        # 发送数据到mqtt服务器
        publish.single("temperature",
                       payload="%s" % info,  # 传送内容
                       hostname="127.0.0.1",  # 你的ip地址
                       client_id="lora1",
                       port=1883,
                       protocol=mqtt.MQTTv311)

    # 房间的传感器数据：
    for i in range(4):
        room_id = i + 1
        time0 = time.strftime("%Y-%m-%d %H:%M:%S")
        #     房间温度
        temperature = random.uniform(20, 30)
        # 整合信息
        info = "'" + str(time0) + "','" + str(temperature) + "','0','" + str(room_id) + "'"
        publish.single("temperature",
                       payload="%s" % info,  # 传送内容
                       hostname="127.0.0.1",  # 你的ip地址
                       client_id="lora1",
                       port=1883,
                       protocol=mqtt.MQTTv311)
        #     房间湿度
        humidity = random.uniform(0.1, 0.9)
        # 整合信息
        info = "'" + str(time0) + "','" + str(humidity) + "','" + str(room_id) + "'"
        publish.single("humidity",
                       payload="%s" % info,  # 传送内容
                       hostname="127.0.0.1",  # 你的ip地址
                       client_id="lora3",
                       port=1883,
                       protocol=mqtt.MQTTv311)
        #     房间人数
        number_of_people = random.randint(0, 10)
        info = "'" + str(time0) + "','" + str(number_of_people) + "','" + str(room_id) + "'"
        publish.single("people",
                       payload="%s" % info,  # 传送内容
                       hostname="127.0.0.1",  # 你的ip地址
                       client_id="lora4",
                       port=1883,
                       protocol=mqtt.MQTTv311)
    # 延时模拟
    time.sleep(2)