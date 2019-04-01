import serial
import time
import binascii
import re

f = open("C:\\Users\\Jonathan\\Desktop\\test\\test test\\queue\\workspace\\reply.txt", "r")
ser = serial.Serial("COM22", 115200)
for line in f:

    arr = bytearray.fromhex(line.split(";")[0])
    for val in arr:
        print(format(val, "02x"))
    ser.write(arr)


#while True:
#    str = f.readline()
#    print (str)
#    if str == "":
#        break

#ser.write(bytes("0C 04", 'utf-8'))
#ser.write(bytes([0X0c,0x04]))
