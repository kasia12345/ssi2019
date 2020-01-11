class Classification:

    def __init__(self, decision=0, indexList=0):
        self.cObject = ""
        self.listOfClassifiedCorrectly = 0
        self.listOfClassified = 0

    def setCObject(self, a):
        self.cObject = a

    def setListOfClassifiedCorrectly(self, a):
        self.listOfClassifiedCorrectly = a

    def setListOfClassified(self, a):
        self.listOfClassified = a

    def getCObject(self):
        return self.cObject

    def getListOfClassifiedCorrectly(self):
        return self.listOfClassifiedCorrectly

    def getListOfClassified(self):
        return self.listOfClassified
