class Favorization:

    def __init__(self, decision=0, whichElem=0, testObject=0):
        self.decision = ""
        self.whichElem = 0
        self.testObject=""

    def setDecision(self, a):
        self.decision = a

    def setWhichElem(self, a):
        self.whichElem = a

    def setTestObject(self, a):
        self.testObject = a

    def getDecision(self):
        return self.decision

    def getWhichElem(self):
        return self.whichElem

    def getTestObject(self):
        return self.testObject