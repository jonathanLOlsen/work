class NeoModule:
    port = ""
    nodeId = ""

    def __init__(self, port, nodeId):
        self.port = port
        self.nodeId = nodeId

    def display(self):
        print("port nr " + str(self.port))
        print("nodeId " + str(self.nodeId))

    def send(self):
        hexStr = ("03 0c 00 " + self.nodeId + " 00 01 02 03 04 05 06 07 08 09")
        print ("hexstr: " + hexStr)
        print("neomod id: " +  self.nodeId)
        return(bytearray.fromhex(hexStr))
#obj = NeoModule("COM21","00 20")
#obj1 = NeoModule("COM17",10)

#obj.display()
#obj.send()
#obj1.send()
