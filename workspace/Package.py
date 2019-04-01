class Package:
    name = ""
    type = 0
    minL = 0
    maxL = 0

    def __init__(self, name, type, minL, maxL):
        self.name = name
        self.type = type
        self.minL = minL
        self.maxL = maxL


    def tp(val):
        if val == (b'\x59'):
            return Package("nList",59,20,30)
        elif val == (b'\x58'):
            return 123213

        elif val == (b'\x52'):
            return Package("uAck",51, 11,17)
        elif val == (b'\x50'):
            return Package("ack",50,12,16)
