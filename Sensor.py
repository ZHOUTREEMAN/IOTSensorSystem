# encoding: utf-8
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

idx = 0  # 往paho/temperature 一直发送内容
while True:
    print("send success")
    publish.single("paho/temperature",
                   payload="this is message:%s" % idx,  # 传送内容
                   hostname="127.0.0.1",  # 你的ip地址
                   client_id="lora1",
                   # qos = 0,
                   # tls=tls,
                   port=1883,
                   protocol=mqtt.MQTTv311)
    idx += 1