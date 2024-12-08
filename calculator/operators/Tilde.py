from operators.Operator import Operator

class Tilde(Operator):

    def getSymbol(self):
        return '~'

    def getPosition(self):
        return "left"

    def getPriority(self):
        return 6
    def operate(self,num):
        return -num
