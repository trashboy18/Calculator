from operators.Operator import Operator

class Hashtag(Operator):

    def getSymbol(self):
        return '#'

    def getPosition(self):
        return "right"

    def getPriority(self):
        return 6
    def operate(self,num):
        num = str(num).replace('.','')
        num = int(num)
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum
