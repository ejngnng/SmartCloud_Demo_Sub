#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import requests
import json
import time

subBroker = "localhost"
subTopic = ['device/device_register', 'device/device_operate', 'device/status_update', 'device/status_reply']
subUrl = ['http://localhost/index.php/mqtt/sub/register', 'http://localhost/index.php/mqtt/sub/operate', 'http://localhost/index.php/mqtt/sub/update', 'http://localhost/index.php/mqtt/sub/overall']

def on_message(mq, userdata, msg):
    print("topic: " + msg.topic + " " + "msg: " + msg.payload)
    if(msg.topic == subTopic[0]):
        requests.post(subUrl[0], msg.payload)

    if(msg.topic == subTopic[1]):
        requests.post(subUrl[1], msg.payload)

    if(msg.topic == subTopic[2]):
        requests.post(subUrl[2], msg.payload)

    if(msg.topic == subTopic[3]):
        requests.post(subUrl[3], msg.payload)

class Sub:
    __topic = ""
    __broker = ""
    __mqttClient = mqtt.Client()

    def __init__(self, broker):
        self.__topic = subTopic
        self.__broker = broker
        self.__mqttClient.connect(self.__broker)

    def start(self):
        self.__mqttClient.subscribe(self.__topic[0])
        self.__mqttClient.subscribe(self.__topic[1])
        self.__mqttClient.subscribe(self.__topic[2])
        self.__mqttClient.subscribe(self.__topic[3])
        self.__mqttClient.on_message = on_message
        self.__mqttClient.loop_forever()



def main():
    register = Sub(subBroker)
    register.start()




if __name__ == '__main__':
    main()
