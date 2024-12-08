from operators.Operator import Operator

class Mod(Operator):

    def getSymbol(self):
        return '%'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 4
    def operate(self,num1,num2):
        return num1 % num2