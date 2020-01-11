import re
import random
from Decision import Decision
from Param import Param
from Classification import Classification
from Favorization import Favorization


def listAttributesAndTheirNumbers(self):
    lines = splitIntoLines(self)
    myArray = []
    for line in lines:
        myArray.append(line.split(" "))
    return myArray


def printFile(self):
    f = open(self)
    print(f.read())


def splitIntoLines(self):
    return re.split(r'\n', self)


def delLastColumnAndRow(self):
    for i in range(len(self)):
        del self[i][len(self[i]) - 1]
    del self[len(self) - 1]
    return self


def switchColumnsToRows(self):
    result = []
    for x in range(len(self[0])):
        row = []
        for i in range(len(self)):
            a = len(self)
            row.append(self[i][x])
        result.append(row)
    return result


def getDecisions(array):
    result = []
    for i in range(len(array)):
        if not array[i][len(array[i]) - 1] in result:
            result.append(array[i][len(array[i]) - 1])
    return result


def getIndexOfDecision(array):
    decisions = getDecisions(array)
    result = []
    for x in decisions:
        decisionObject = Decision()
        decisionObject.setDecision(x)
        list = []
        for i in range(len(array)):
            if array[i][len(array[i]) - 1] == x:
                list.append(i)
        decisionObject.setIndexList(list)
        result.append(decisionObject)
    return result


def countParam(array, trnArray):
    i = 0
    indexOfDecisions = getIndexOfDecision(trnArray)
    listOfDecisions = []
    for checkOtherDecisions in indexOfDecisions:
        listOfDecisions.append(checkOtherDecisions.getDecision())
    favorizationList = []
    listOfParam = []
    for xX in array:
        i += 1
        param = Param()
        for decision in indexOfDecisions:
            param = Param()
            param.setTestObject("x" + str(i))
            param.setCObjet(decision.getDecision())
            listOfParamCounter = []
            whichElem = 0
            for elemOfX in xX:
                if whichElem == len(xX) - 1:
                    continue
                counter = 0
                for k in decision.getIndexList():
                    if elemOfX == trnArray[k][whichElem]:
                        counter += 1

                # check if other c has 0 objects
                # if true counter += 1
                incrementByOne = True
                for elem in indexOfDecisions:
                    if elem.getDecision() != decision.getDecision():
                        for j in elem.getIndexList():
                            if elemOfX == trnArray[j][whichElem] or counter == 0:
                                incrementByOne = False
                                break

                if (incrementByOne == True):
                    counter += 1

                if (counter == 0):
                    checkIfAllZero = True
                    for k in range(len(trnArray) - 1):
                        if elemOfX == trnArray[k][whichElem]:
                            checkIfAllZero = False
                            break

                    if checkIfAllZero == False:
                        favorization = Favorization()
                        favorization.setDecision(decision.getDecision())
                        favorization.setWhichElem(whichElem)
                        favorization.setTestObject(param.getTestObject())
                        favorizationList.append(favorization)
                whichElem += 1
                listOfParamCounter.append(counter / len(decision.getIndexList()))
            paramResult = (len(decision.getIndexList()) / len(trnArray)) * sum(listOfParamCounter)
            param.setParam(paramResult)
            listOfParam.append(param)

    for elem in listOfParam:
        for favorization in favorizationList:
            if elem.getTestObject() == favorization.getTestObject() and elem.getCObject() != favorization.getDecision():
                length = 0
                for decisionElem in indexOfDecisions:
                    if decisionElem.getDecision() == elem.getCObject():
                        length = len(decisionElem.getIndexList())
                elem.setParam(elem.getParam() + ((1 / 2) * (1 / length)))
    return listOfParam


def getGlobalAccuracy(classificationList):
    sumOfCorrectlyClassified = 0
    sumOfAllObjects = 0
    for elem in classificationList:
        sumOfCorrectlyClassified += elem.getListOfClassifiedCorrectly()
        sumOfAllObjects += elem.getListOfClassified()
    return sumOfCorrectlyClassified / sumOfAllObjects


def getBalancedAccuracy(allClasses, classificationList):
    fraction = 0
    for elem in classificationList:
        fraction += (elem.getListOfClassifiedCorrectly() / elem.getListOfClassified())
    return fraction / len(allClasses)


def numOfCorrectlyClassified(listOfCountedParams, listOfDecisionsInTST, textFile):
    listOfClassifications = []
    i = 1
    listOfParamsInLoop = []
    properlyClassified = 0
    classified = 0

    for uDecision in unique(listOfDecisionsInTST):
        classification = Classification()
        classification.setCObject(uDecision)
        classification.setListOfClassified(0)
        classification.setListOfClassifiedCorrectly(0)
        listOfClassifications.append(classification)

    enum = 0
    for countedParam in listOfCountedParams:
        xObject = "x" + str(i)
        if xObject == countedParam.getTestObject():
            listOfParamsInLoop.append(countedParam)

        if xObject != listOfCountedParams[enum + 1].getTestObject() or \
                len(listOfDecisionsInTST) == 1 and len(listOfParamsInLoop) == 2:
            cObject = ""
            param = 0
            highestX = ""
            listOfParamsInLoopIterator = 0
            for elem in listOfParamsInLoop:
                if param < elem.getParam():
                    param = elem.getParam()
                    highestX = elem.getTestObject()
                    cObject = elem.getCObject()
                    listOfParamsInLoopIterator += 1

            if listOfParamsInLoopIterator > 1:
                textFile.write("Param c==" + listOfParamsInLoop[0].getCObject() + "<" + "Param C==" + listOfParamsInLoop[
                    len(listOfParamsInLoop)-1].getCObject() + " dla obiektu " + highestX)
            if listOfParamsInLoopIterator <= 1:
                textFile.write("Param c==" + listOfParamsInLoop[0].getCObject() + ">" + "Param C==" + listOfParamsInLoop[
                    len(listOfParamsInLoop)-1].getCObject() + " dla obiektu " + highestX)

            # textFile.write("Dla "+highestX+" param c=="+cObject+" jest największe\n")
            if areParamsInLoopEqual(listOfParamsInLoop):
                randomParam = random.choice(listOfParamsInLoop)
                if randomParam.getCObject() == listOfDecisionsInTST[i - 1]:
                    textFile.write(" ta decyzja jest zgodna z ukryta decyzja eksperta (decyzja eksperta == " +
                                   listOfDecisionsInTST[i - 1] + ")\n")
                    for element in listOfClassifications:
                        if element.getCObject() == randomParam.getCObject():
                            element.setListOfClassifiedCorrectly(element.getListOfClassifiedCorrectly() + 1)
                            element.setListOfClassified(element.getListOfClassified() + 1)

                else:
                    textFile.write(" ta decyzja jest nie zgodna z ukryta decyzja eksperta (decyzja eksperta == " +
                                   listOfDecisionsInTST[i - 1] + ")\n")
                    for element in listOfClassifications:
                        if element.getCObject() == randomParam.getCObject():
                            element.setListOfClassified(element.getListOfClassified() + 1)
            else:
                if cObject == listOfDecisionsInTST[i - 1]:
                    textFile.write(" ta decyzja jest zgodna z ukryta decyzja eksperta (decyzja eksperta == " +
                                   listOfDecisionsInTST[i - 1] + ")\n")
                    for element in listOfClassifications:
                        if element.getCObject() == cObject:
                            element.setListOfClassifiedCorrectly(element.getListOfClassifiedCorrectly() + 1)
                            element.setListOfClassified(element.getListOfClassified() + 1)
                else:
                    textFile.write(" ta decyzja jest nie zgodna z ukryta decyzja eksperta (decyzja eksperta == " +
                                   listOfDecisionsInTST[i - 1] + ")\n")
                    for element in listOfClassifications:
                        if element.getCObject() == cObject:
                            element.setListOfClassified(element.getListOfClassified() + 1)
            i += 1
            listOfParamsInLoop = []
        enum += 1
        if enum == len(listOfCountedParams) - 1:
            enum = 0

    return listOfClassifications


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def getListOfDecisionsTST(array):
    result = []
    for row in array:
        result.append(row[len(row) - 1])
    return result


def areParamsInLoopEqual(paramsInLoop):
    x = []
    for elem in paramsInLoop:
        x.append(elem.getParam())
    if len(unique(x)) == 1:
        return True
    return False


def incrementIfotherObjectEqualsZero():
    print("a")

def louFromIndexToList(index, list):
    result = []
    result.append(list[index])
    return result

def fromIndexToList(indexList, list):
    result = []
    for i in indexList:
        result.append(list[i])
    return result

def splitIntoNPartsLOU(array, kParts):
    kPartLen = len(array) / kParts
    indexList = []

    for i in range(kParts):
        indexForParts = []
        j = 0
        while j < int(kPartLen):
            rand = random.randint(0, len(array) - 1)
            otherPartsContains = False
            for elem in indexList:
                if elem.__contains__(rand):
                    otherPartsContains = True

            if (not indexForParts.__contains__(rand) and otherPartsContains == False):
                indexForParts.append(rand)
            else:
                j -= 1
            j += 1
        indexList.append(indexForParts)
    return indexList

def splitIntoKParts(array, kParts):
    kPartLen = len(array)/kParts
    indexList=[]

    for i in range(kParts):
        indexForParts = []
        j = 0
        while j < int(kPartLen):
            rand = random.randint(0, len(array) - 1)
            otherPartsContains = False
            for elem in indexList:
                if elem.__contains__(rand):
                    otherPartsContains = True

            if (not indexForParts.__contains__(rand) and otherPartsContains == False):
                indexForParts.append(rand)
            else:
                j -= 1
            j += 1
        indexList.append(indexForParts)
    return indexList