import sys

from operators.Operator import Operator
from math import pow
from Exceptions import InvalidPowerValues
class Power(Operator):

    def getSymbol(self):
        return '^'

    def getPosition(self):
        return "middle"

    def getPriority(self):
        return 3
    def operate(self,base,exp):
        if base < 0 and (not exp.is_integer()):
            raise InvalidPowerValues(f"cannot root a negative number: {base}")
        if base > 1 and exp > pow(sys.float_info.max,(1/base)):
            raise InvalidPowerValues("Exponentiation result will exceed float max limit.")
        if base == 0 and exp < 0:
            raise InvalidPowerValues("exponential can't be negative while base is zero")
        try:
            res=pow(base,exp)
            if res > 1.7976931348623157e+308 or res < 5e-324:
                raise OverflowError()
        except OverflowError:
            raise InvalidPowerValues("the result is too big to handle!")


        return pow(base,exp)