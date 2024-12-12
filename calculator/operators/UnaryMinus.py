from operators.Operator import Operator

class UnaryMinus(Operator):
    def getSymbol(self):
        return 'unary_minus'

    def getPosition(self):
        return "left"

    def getPriority(self):
        return 2.5

    def operate(self, num):
        return -num
