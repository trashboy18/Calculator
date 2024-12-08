from operators.Operator import Operator


class Factorial(Operator):

    def getSymbol(self):
        return '!'

    def getPosition(self):
        return "right"

    def getPriority(self):
        return 6
    def operate(self,num):
        return
