from operators.Operator import Operator
from Exceptions import InvalidHashtagValue
class Hashtag(Operator):

    def getSymbol(self):
        return '#'

    def getPosition(self):
        return "right"

    def getPriority(self):
        return 6
    @staticmethod
    def operate(num):
       # num.startswith("-") raise...
        if num.startswith('-'):
            raise InvalidHashtagValue(f"cant perform # on a negative number: {num}")
        num = str(num).replace('.','')

        if 'e' in num:
            raise InvalidHashtagValue("Number is too big for #")
        num = int(num)
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum
