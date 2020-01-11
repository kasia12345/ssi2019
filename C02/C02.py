import Common
from Param import Param

class NaiwnyKlasyfikatorBayesa():
    def main(self):
        fDec = open("result/dec_bayes.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian_TST.txt").read())
        australianTRNList = Common.listAttributesAndTheirNumbers(open("australian_TRN.txt").read())
        lines = Common.delLastColumnAndRow(lines)
        australianTRNList = Common.delLastColumnAndRow(australianTRNList)
        getTrnDecisions = Common.getIndexOfDecision(australianTRNList)
        getDecisions = Common.getIndexOfDecision(lines)
        countedParams = Common.countParam(lines, australianTRNList)
        classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(lines), fDec)
        globalAccuracy = Common.getGlobalAccuracy(classified)
        allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
        print("Global accuracy = "+str(globalAccuracy))
        print("Balanced accuracy = "+str(Common.getBalancedAccuracy(allClasses, classified)))
        fAcc = open("result/acc_bayes.txt", "w+")
        fAcc.write(f"Global accuracy = "+str(globalAccuracy)+"\nBalancedAccuracy = "+ str(Common.getBalancedAccuracy(allClasses, classified)))


if __name__ == "__main__":
    NaiwnyKlasyfikatorBayesa.main("args")

