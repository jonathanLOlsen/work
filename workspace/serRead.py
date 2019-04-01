import serial
import time
import binascii
import queue
import Package
import circularlist
import thread

ser = serial.Serial("COM23", 115200)

eventList = [b'\x59',b'\x58',"\x52","\x50"]
#ack = pakketype (59,20,25)

def event(val):
    print(val.hex() + "i event")
    if val in eventList:
        return True
    else:
        print("false")


q = queue.Queue()
c = circularlist.circularlist(32)



while True:
    if c.index < 32:
        #print(ser.inWaiting())
        xx = ser.read()
        #print(xx)
        c.append(xx)
        print(c)
        print(c._data)
        print(c.size)
        print(c.index)
    else:
        time.sleep(1)

    #print(Package.Package.tp(xx))
    #if not c.empty():
    #    while q.empty() == False:
    #        print("we are in the second while loop")
    #        t = event(q.get())
    #        print (t)
#
    #        if t == True:
    #            print("we got to the if statment")
    #            print(q.get())
    #            i = 0
#
    #            while int(asd) > i:
    #                print (q.get())
    #                i = i + 1
