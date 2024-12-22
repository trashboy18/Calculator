from operators.Operator import Operator
from Exceptions import InvalidFactorialValue
from colorama import Fore,Style

class Factorial(Operator):

    def getSymbol(self):
        return '!'

    def getPosition(self):
        return "right"

    def getPriority(self):
        return 6
    def operate(self,num):
        if num < 1:
            raise InvalidFactorialValue(f"cant factorial a negative number: "
                                        f"{num}")
        if num > 170:
            raise InvalidFactorialValue(f"the number {num} is too big to factorial")
        if not float(num).is_integer():
            raise InvalidFactorialValue(f"can't factorial a decimal number : {num}")
        result = 1
        for i in range(1,int(num)+1):
            result*=i
        return result