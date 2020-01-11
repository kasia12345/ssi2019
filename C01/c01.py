import math
import re
from KlasaDecyzyjna import KlasaDecyzyjna


class SystemDecyzyjny:
    NUMBER_OF_ATTRIBUTES = 15

    def printFile(self):
        f = open(self)
        print(f.read())

    def getNumericAttributes(self):
        i = 0
        array = []
        for elem in self:
            if "n" in elem:
                array.append(i)
            i += 1
        return array

    def minAttributeValue(self, numericAttributes):
        for i in numericAttributes:
            array = []
            for x in range(len(self)):
                array.append(self[x][i])
            print("attribute", i, "min value", min(array))

    def maxAttributeValue(self, numericAttributes):
        for i in numericAttributes:
            array = []
            for x in range(len(self)):
                array.append(self[x][i])
            print("attribute", i, "max value", max(array))

    def separateClasses(self):
        result = []
        for i in self:
            result.append(i[0:3])
        return result

    def sortAttrToSpecifiedClass(listOfClasses, listOfAttributes):
        result = []
        listIteration = 0
        for i in listOfClasses:
            x = KlasaDecyzyjna()
            x.setKlasaDecyzyjna(i)
            attributes = SystemDecyzyjny.switchColumnsToRows(listOfAttributes)
            x.setAttributes(attributes[listIteration])
            listIteration += 1
            result.append(x)
        return result

    def switchColumnsToRows(self):
        result = []
        for x in range(len(self[0])):
            row = []
            for i in range(len(self)):
                row.append(self[i][x])
            result.append(row)
        return result

    def average(self):
        sum = 0
        for i in self:
            sum = sum + float(i)
        return sum / len(self)

    def numberOfAttributesInClass(classes, numeric):
        for i in range(len(classes)):
            print(KlasaDecyzyjna.getKlasaDecyzyjna(classes[i]), "has", len(KlasaDecyzyjna.getAttributes(classes[i])),
                  "attributes")

    def standardDeviation(classes, numeric):
        for i in numeric:
            standDevList = KlasaDecyzyjna.getAttributes(classes[i])
            standDevAvg = SystemDecyzyjny.average(standDevList)
            sum = 0
            for j in standDevList:
                xi = float(j) - standDevAvg
                xi2 = xi * xi
                sum = sum + xi2
            standDev = math.sqrt(sum / len(standDevList))
            print(KlasaDecyzyjna.getKlasaDecyzyjna(classes[i]), "standard deviation:", standDev)

    def splitIntoLines(self):
        return re.split(r'\n', self)

    def listAttributesAndTheirNumbers(self):
        lines = SystemDecyzyjny.splitIntoLines(self)
        myArray = []
        for line in lines:
            myArray.append(line.split(" "))
        return myArray


def main():
    # SystemDecyzyjny.printFile("C01/australian-type.txt")
    array = SystemDecyzyjny.splitIntoLines(open("C01/australian-type.txt").read())
    print(array)
    lines = SystemDecyzyjny.listAttributesAndTheirNumbers(open("C01/australian.txt").read())
    SystemDecyzyjny.minAttributeValue(lines, SystemDecyzyjny.getNumericAttributes(array))
    SystemDecyzyjny.maxAttributeValue(lines, SystemDecyzyjny.getNumericAttributes(array))
    SystemDecyzyjny.switchColumnsToRows(SystemDecyzyjny.listAttributesAndTheirNumbers(open("C01/australian.txt").read()))
    classes = SystemDecyzyjny.sortAttrToSpecifiedClass(SystemDecyzyjny.separateClasses(array), SystemDecyzyjny.listAttributesAndTheirNumbers(open("C01/australian.txt").read()))
    SystemDecyzyjny.numberOfAttributesInClass(classes, SystemDecyzyjny.switchColumnsToRows(
    SystemDecyzyjny.listAttributesAndTheirNumbers(open("C01/australian.txt").read())))
    SystemDecyzyjny.standardDeviation(classes, SystemDecyzyjny.getNumericAttributes(array))


if __name__ == "__main__":
    main()