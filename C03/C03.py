import Common
import random


class TrainAndTest():
    def main(self):
        print("T&T")
        fDec = open("result/dec_bayesT&T.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        randomSystemIndexList = TrainAndTest.generateTRNandTSTIndexList(lines, 0.5)
        randomTrnSystem = Common.fromIndexToList(randomSystemIndexList[0], lines)
        randomTstSystem = Common.fromIndexToList(randomSystemIndexList[1], lines)
        countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
        classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem), fDec)
        globalAccuracy = Common.getGlobalAccuracy(classified)
        allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
        print("Global accuracy = " + str(globalAccuracy))
        print("Balanced accuracy = " + str(Common.getBalancedAccuracy(allClasses, classified)))
        fAcc = open("result/acc_bayesT&T.txt", "w+")
        fAcc.write(f"Global accuracy = " + str(globalAccuracy) + "\nBalancedAccuracy = " + str(
            Common.getBalancedAccuracy(allClasses, classified)))
        print("\n")

    # Returns 2d array
    # Row #1 - trn array
    # Row #2 - tst array
    # T&T
    def generateTRNandTSTIndexList(array, ratio):
        arrayLen = len(array)
        result = []
        trnArray = []
        tstArray = []
        for i in range(int(arrayLen * ratio)):
            k = random.randint(0, arrayLen - 1)
            if (not trnArray.__contains__(k)):
                trnArray.append(k)
            else:
                i -= 1

        result.append(trnArray)

        for j in range(arrayLen):
            if not trnArray.__contains__(j):
                tstArray.append(j)
        result.append(tstArray)
        return result

    def fromIndexToList(indexList, list):
        result = []
        for i in indexList:
            result.append(list[i])
        return result


class BootstrapMethod():

    # Returns 2d array
    # Row #1 - trn array
    # Row #2 - tst array
    # T&T
    def generateTRNandTSTIndexList(array):
        arrayLen = len(array)
        result = []
        trnArray = []
        tstArray = []
        for i in range(arrayLen):
            k = random.randint(0, arrayLen - 1)
            trnArray.append(k)

        result.append(trnArray)

        for j in range(arrayLen):
            if not trnArray.__contains__(j):
                tstArray.append(j)
        result.append(tstArray)
        return result


class MonteCarloCV():
    def main(self):
        print("MCCV")
        folds = 5
        ratio = 0.5
        listOfGlobAcc = []
        listOfBalAcc = []
        fDec = open("result/dec_bayesMCCV.txt", "w+")
        for i in range(folds):
            fDec.write(
                f"///////////////////////////////  FOLD NUMBER " + str(i + 1) + "  ///////////////////////////////\n")
            lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
            randomSystemIndexList = TrainAndTest.generateTRNandTSTIndexList(lines, ratio)
            randomTrnSystem = Common.fromIndexToList(randomSystemIndexList[0], lines)
            randomTstSystem = Common.fromIndexToList(randomSystemIndexList[1], lines)
            countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
            classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem),
                                                         fDec)
            globalAccuracy = Common.getGlobalAccuracy(classified)
            allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
            listOfGlobAcc.append(globalAccuracy)
            listOfBalAcc.append(Common.getBalancedAccuracy(allClasses, classified))

        fAcc = open("result/acc_bayesMCCV.txt", "w+")
        fAcc.write(f"Global accuracy = " + str((sum(listOfGlobAcc) / folds)) + "\nBalancedAccuracy = " + str(
            (sum(listOfBalAcc) / folds)))

        print("Average Global accuracy for " + str(folds) + " folds = " + str((sum(listOfGlobAcc) / folds)))
        print("Average Balanced Accuracy for " + str(folds) + " folds = " + str((sum(listOfBalAcc) / folds)))
        print("\n")

class Bagging():
    def main(self):
        print("Bagging")
        fDec = open("result/dec_bayesBagging.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        folds = 5
        listOfGlobAcc = []
        listOfBalAcc = []
        for i in range(folds):
            randomSystemIndexList = BootstrapMethod.generateTRNandTSTIndexList(lines)
            randomTrnSystem = Common.fromIndexToList(randomSystemIndexList[0], lines)
            randomTstSystem = Common.fromIndexToList(randomSystemIndexList[1], lines)
            countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
            classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem), fDec)

            globalAccuracy = Common.getGlobalAccuracy(classified)
            allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
            listOfGlobAcc.append(globalAccuracy)
            listOfBalAcc.append(Common.getBalancedAccuracy(allClasses, classified))

        fAcc = open("result/acc_bayesBagging.txt", "w+")
        fAcc.write(f"Global accuracy = " + str((sum(listOfGlobAcc) / folds)) + "\nBalancedAccuracy = " + str(
            (sum(listOfBalAcc) / folds)))
        print("Average Global accuracy for " + str(folds) + " folds = " + str((sum(listOfGlobAcc) / folds)))
        print("Average Balanced Accuracy for " + str(folds) + " folds = " + str((sum(listOfBalAcc) / folds)))
        print("\n")

class CrossValidation():
    def main(self):
        print("Cross Validation")
        fDec = open("result/dec_bayesCV.txt", "w+")
        k=5
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        randomSystemIndexList = Common.splitIntoKParts(lines, k)
        listOfGlobAcc = []
        listOfBalAcc = []
        for i in range(len(randomSystemIndexList)):
            fDec.write(
                f"///////////////////////////////  FOLD NUMBER " + str(i + 1) + "  ///////////////////////////////\n")
            randomTstSystem = []
            trnIndexList = []
            for j in range(len(randomSystemIndexList)):
                if j != i:
                    for elem in randomSystemIndexList[j]:
                        trnIndexList.append(elem)
            randomTstSystem = Common.fromIndexToList(randomSystemIndexList[i], lines)
            randomTrnSystem = Common.fromIndexToList(trnIndexList, lines)
            countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
            classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem),
                                                         fDec)
            globalAccuracy = Common.getGlobalAccuracy(classified)
            allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
            listOfGlobAcc.append(globalAccuracy)
            listOfBalAcc.append(Common.getBalancedAccuracy(allClasses, classified))
        fAcc = open("result/acc_bayesCV.txt", "w+")
        fAcc.write(f"Global accuracy = " + str((sum(listOfGlobAcc) / k)) + "\nBalancedAccuracy = " + str(
            (sum(listOfBalAcc) / k)))
        print("Average Global accuracy for " + str(k) + " folds = " + str((sum(listOfGlobAcc) / k)))
        print("Average Balanced Accuracy for " + str(k) + " folds = " + str((sum(listOfBalAcc) / k)))
        print("\n")

class LeaveOneOut():
    def main(self):
        print("Leave One Out")
        fDec = open("result/dec_bayesLOU.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        k = len(lines)
        systemIndexList = []
        for row in range(len(lines)):
            systemIndexList.append(row)

        listOfGlobAcc = []
        listOfBalAcc = []
        for i in range(len(systemIndexList)):
            fDec.write(
                f"///////////////////////////////  FOLD NUMBER " + str(i + 1) + "  ///////////////////////////////\n")
            randomTstSystem = []
            trnIndexList = []
            for j in range(len(systemIndexList)):
                if j != i:
                    trnIndexList.append(j)
            randomTstSystem = Common.louFromIndexToList(systemIndexList[i], lines)
            randomTrnSystem = Common.fromIndexToList(trnIndexList, lines)
            countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
            classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem),
                                                         fDec)
            allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
            if classified[0].getListOfClassified() != 0:
                globalAccuracy = Common.getGlobalAccuracy(classified)
                balancedAccuracy = Common.getBalancedAccuracy(allClasses, classified)
            else:
                globalAccuracy = 0
                classified[0].setListOfClassified(classified[0].getListOfClassified()+1)
                balancedAccuracy = Common.getBalancedAccuracy(allClasses, classified)

            listOfGlobAcc.append(globalAccuracy)
            listOfBalAcc.append(balancedAccuracy)
        fAcc = open("result/acc_bayesLOU.txt", "w+")
        fAcc.write(f"Global accuracy = " + str((sum(listOfGlobAcc) / k)) + "\nBalancedAccuracy = " + str(
            (sum(listOfBalAcc) / k)))
        print("Average Global accuracy for " + str(k) + " folds = " + str((sum(listOfGlobAcc) / k)))
        print("Average Balanced Accuracy for " + str(k) + " folds = " + str((sum(listOfBalAcc) / k)))


if __name__ == "__main__":
    TrainAndTest.main("args")
    MonteCarloCV.main("args")
    Bagging.main("args")
    CrossValidation.main("args")
    LeaveOneOut.main("args")