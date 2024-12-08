from operators.Operator import Operator

class Minimum(Operator):

    def getSymbol(self):
        return '&'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 5
    def operate(self,num1,num2):
        return num1 if num1 < num2 else num2
