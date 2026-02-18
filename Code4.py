from machine import Pin

import time

in_list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

in1 = Pin(14, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(27, Pin.OUT)

pb1 = Pin(22, Pin.IN, Pin.PULL_UP)
pb2 = Pin(18, Pin.IN, Pin.PULL_UP)

while True:
    button1 = pb1.value()
    button2 = pb2.value()
    
    if button1 == 0 and button2 == 1:
        for _ in range(0,500):
            for i in in_list:
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                time.sleep(0.005)
    
    if button1 == 1 and button2 == 0:
        for _ in range(0,500):
            for i in reversed(in_list):
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                time.sleep(0.005)
            
