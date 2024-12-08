from operators.Operator import Operator

class Divide(Operator):

    def getSymbol(self):
        return '/'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 2
    def operate(self,num1,num2):
        return float(num1 / num2)