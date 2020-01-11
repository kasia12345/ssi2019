class  Param:

    def __init__(self, testObject=0, cObjet=0, param=0):
        self.testObject = ""        # x1,x2 etc.
        self.cObjet = ""            # c=1, c=0
        self.param = 0              # result

    def setTestObject(self, a):
        self.testObject = a

    def setCObjet(self, a):
        self.cObjet = a

    def setParam(self, a):
        self.param = a

    def getTestObject(self):
        return self.testObject

    def getCObject(self):
        return self.cObjet

    def getParam(self):
        return self.param
