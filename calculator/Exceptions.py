# Base Exception
class CalculatorException(Exception):
    """Base class for calculator exceptions."""
    def __init__(self, message):
        super().__init__(message)


# Specific Exceptions
class InvalidCharException(CalculatorException):
    """Raised when an invalid character is encountered."""
    pass


class DivisionValueError(CalculatorException):
    """Raised when attempting to divide by zero."""
    pass


class InvalidFactorialValue(CalculatorException):
    """Raised when an invalid number is factorialed."""
    pass


class InvalidOperatorSequence(CalculatorException):
    """Raised when operators are not positioned correctly."""
    pass


class InvalidOperatorsTrail(CalculatorException):
    """Raised when operators are trailing with nothing after them."""
    pass


class InvalidHashtagValue(CalculatorException):
    """Raised when an invalid number is hashtaged."""
    pass


class InvalidOperatorPlacement(CalculatorException):
    """Raised when an operator is not placed correctly."""
    pass


class InvalidParenthesesUse(CalculatorException):
    """Raised if parentheses are not used correctly."""
    pass


class InvalidMultipleDots(CalculatorException):
    """Raised if there is more than one dot in a number."""
    pass


class InvalidPowerValues(CalculatorException):
    """Raised if the user tries to root a negative number."""
    pass


class InvalidEmptyExpression(CalculatorException):
    """Raised if the expression is empty."""
    pass


class ResultUnrepresentable(CalculatorException):
    """Raised if the result is too big to handle."""
    pass
