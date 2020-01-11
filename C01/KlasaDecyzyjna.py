class  KlasaDecyzyjna:

    def __init__(self, klasaDecyzyjna=0, attributes=0):
        self.klasaDecyzyjna = ""
        self.attributes = []

    def setKlasaDecyzyjna(self, a):
        self.klasaDecyzyjna = a

    def setAttributes(self, a):
        self.attributes = a

    def getKlasaDecyzyjna(self):
        return self.klasaDecyzyjna

    def getAttributes(self):
        return self.attributes