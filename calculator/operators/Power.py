from operators.Operator import Operator
from math import pow
class Power(Operator):

    def getSymbol(self):
        return '^'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 3
    def operate(self,num1,num2):
        return pow(num1,num2)