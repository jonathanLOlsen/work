import NeoModule
import Serial







def Main():

    NeoModule.obj = NeoModule.NeoModule("COM20","20")
    port = NeoModule.obj.port
    print(port)
    data = NeoModule.obj.send()
    print(data)
    Serial.obj = Serial.Serial(port, 9600, data)
    #NeoModule.obj.display()
    Serial.obj.read()


if __name__ == '__main__':
	Main()
