import sys

from operators.Operator import Operator
from Exceptions import DivisionValueError
from sys import float_info
class Divide(Operator):

    def getSymbol(self):
        return '/'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 2
    def operate(self,num1,num2):
        if abs(num2) < sys.float_info.min:
            raise DivisionValueError("Division by a number too small to represent.")
        if abs(num2) > sys.float_info.max:
            raise DivisionValueError("Division by a number that is too big.")
        if num2 == 0:
            raise DivisionValueError(f"cannot divide by zero: {num1}/{num2}")
        return num1 / num2