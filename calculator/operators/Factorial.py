from operators.Operator import Operator


class Factorial(Operator):

    def getSymbol(self):
        return '!'

    def getPosition(self):
        return "right"

    def getPriority(self):
        return 6
    def operate(self,num):
        result = 1
        for i in range(1,int(num)+1):
            result*=i
        return result