from operators.Operator import Operator

class Power(Operator):

    def getSymbol(self):
        return '^'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 3
    def operate(self,num1,num2):
        return num1 ** num2