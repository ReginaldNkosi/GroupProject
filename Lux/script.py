import codecs
import os
import subprocess
import time
from fileinput import filename
from tokenize import Double

import serial

num_batchs = 0 #chunks of data to be read
data = []
line = ""
filename = "data.txt"
fil =  codecs.open(filename,"a","utf-8")
ser = serial.Serial()
ser.timeout = 10
ser.port = 'COM10'
ser.baudrate =9600
ser.open()

#getting data from stm
while num_batchs!=3:
    for i in range(10):
        line = ser.readline().decode('utf-8','ignore')
        print(line)# COM10
        line = line.strip() #remove whitespace
        line = line.replace("\\", "\\\\")  
    num_batchs+=1

