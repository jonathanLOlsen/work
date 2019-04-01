import serial
import time
import binascii

class Serial:
    port = ""
    baudrate = 9600
    data = ""
    def __init__(self, port, baudrate, data):
        self.port = port
        self.baudrate = baudrate
        self.data = data


    def read(self):
        try:
            ser = serial.Serial(self.port, self.baudrate,timeout=1)
            #ser.close()
            #ser.open()
            print(self.data)
            ser.write(self.data)
            print(ser.write(self.data))
            time.sleep(8)
            read_val = ser.read(size=64)
            print (read_val)
            if read_val is not '':
                print ("")
        except serial.SerialException:
            """asdasdasdasd"""
