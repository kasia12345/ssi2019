class Decision:

    def __init__(self, decision=0, indexList=0):
        self.decision = ""
        self.indexList = []

    def setDecision(self, a):
        self.decision = a

    def setIndexList(self, a):
        self.indexList = a

    def getDecision(self):
        return self.decision

    def getIndexList(self):
        return self.indexList

