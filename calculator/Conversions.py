from Helpers import (
    is_operand,
    resolve_sign_streak,
    attach_unary_minus
)
from colorama import Fore, Style
from Exceptions import *


def tokenize(expression, operators_dic):
    if not expression.strip():
        raise InvalidEmptyExpression("The expression can't be empty!")

    tokens = []
    index = 0
    current_num = ''
    operator_symbols = operators_dic.keys()
    start_of_expression = True

    while index < len(expression):
        char = expression[index]

        if char.isdigit() or char == '.':
            start_of_expression = False
            current_num += char
            index += 1
        elif char in operator_symbols or char in "()":

            if current_num:
                tokens.append(current_num)
                current_num = ''
            if char == '-':
                if start_of_expression:
                    tokens.append('unary_minus')
                else:
                    tokens.append('-')

            else:
                if char == '(':
                    start_of_expression = True
                else:
                    start_of_expression = False
                tokens.append(char)
            index += 1

        else:
            raise InvalidCharException(f"The character '{char}' is not valid in this calculator.")

    if current_num:
        tokens.append(current_num)

    return tokens


def check_validity(tokens, operators_dic):
    operators_symbols = operators_dic.keys()
    index = 0
    while index < len(tokens):
        if is_operand(tokens[index]):

            if index - 1 != -1:
                if (
                        tokens[index - 1] in operators_symbols and
                        operators_dic[tokens[index - 1]].getPosition() == "right"
                ):
                    raise InvalidOperatorPlacement(
                        f"{Fore.RED} The number at index {index} can't have a right position operator: "
                        f"{tokens[index - 1]} on its left {Style.RESET_ALL}"
                    )
                elif tokens[index - 1] == ')':
                    raise InvalidParenthesesUse(
                        f"{Fore.RED} After a: ), there must be an operator.{Style.RESET_ALL}"
                    )
            if index + 1 < len(tokens):
                if (
                        tokens[index + 1] in operators_symbols and
                        operators_dic[tokens[index + 1]].getPosition() == "left"
                ):
                    raise InvalidOperatorPlacement(
                        f"{Fore.RED} The number at index {index} can't have a left position operator: "
                        f"{tokens[index + 1]} on its right {Style.RESET_ALL}"
                    )
                elif tokens[index + 1] == '(':
                    raise InvalidParenthesesUse(
                        f"{Fore.RED} At index {index}, before a: (, there must be an "
                        f"operator.{Style.RESET_ALL}"
                    )
        elif tokens[index] in operators_symbols:
            if (
                    (index == 0 and operators_dic[tokens[index]].getPosition() != "left") or
                    (index == len(tokens) - 1 and operators_dic[tokens[index]].getPosition() != "right")
            ):
                raise InvalidOperatorPlacement(
                    f"{Fore.RED} Operator at index {index} needs to be in the "
                    f"{operators_dic[tokens[index]].getPosition()} of numbers {Style.RESET_ALL}"
                )
            elif operators_dic[tokens[index]].getPosition() == "middle" and tokens[index] != '-':
                if (
                        (index - 1 >= 0 and
                         (tokens[index - 1] == '(' or
                          (tokens[index - 1] in operators_symbols and
                           operators_dic[tokens[index - 1]].getPosition() != "right")))) or \
                        ((index + 1 < len(tokens) and
                          (tokens[index + 1] == ')' or
                           (tokens[index + 1] in operators_symbols and
                            tokens[index + 1] != '-' and
                            operators_dic[tokens[index + 1]].getPosition() != "left")))):
                    raise InvalidOperatorPlacement(
                        f"{Fore.RED} Operator at index {index} needs a number on its left and right"
                    )

            elif operators_dic[tokens[index]].getPosition() == "right":
                if (
                        (index + 1 < len(tokens) and tokens[index + 1] == '(') or
                        (index + 1 < len(tokens) and
                         (tokens[index + 1] in operators_symbols and
                          operators_dic[tokens[index + 1]].getPosition() == "left"))
                ):
                    raise InvalidOperatorPlacement(
                        f"{Fore.RED} Operator at index {index} needs an operator or closing "
                        f"parentheses on its right"
                    )
            elif operators_dic[tokens[index]].getPosition() == "left":
                if index - 1 > -1 and (is_operand(tokens[index - 1]) or tokens[index - 1] == ')'):
                    raise InvalidOperatorPlacement(
                        f"{Fore.RED} Operator at index {index} can't have a number on its left."
                    )
        elif tokens[index] == '(' and index + 1 < len(tokens) and tokens[index + 1] == ')':
            raise InvalidParenthesesUse("Can't have an empty expression inside parentheses")
        index += 1


def normalize_tokens(tokens):
    fixed_tokens = []
    streak = []  # Temporary streak of minuses and tildes
    last_was_operand = False  # Tracks whether the last token was an operand
    if tokens.count('(') != tokens.count(')'):
        raise InvalidParenthesesUse("Mismatched parentheses!")
    for token in tokens:
        if token == '-' or token == '~':
            streak.append(token)
        elif is_operand(token) or token == '(':

            if streak:
                if last_was_operand:
                    if streak.count('~') == 1 and streak[0] != '~' and streak[1] != '~':
                        raise InvalidOperatorPlacement("Tilde can only come after operators "
                                                       "or start of expression")
                    if is_operand(token):
                        fixed_tokens.append('-')
                        streak.pop(0)

                effective_sign = resolve_sign_streak(streak)
                streak.clear()
                if effective_sign:
                    if token == '(' or effective_sign == '~':
                        fixed_tokens.append(effective_sign)
                    else:
                        token = effective_sign + token
                elif token == '(' and last_was_operand:
                    fixed_tokens.append('+')
            fixed_tokens.append(token)
            last_was_operand = is_operand(token)
        elif token == ')':
            if streak:
                raise InvalidOperatorSequence(f"Invalid sequence of operators near {streak + [token]}")
            fixed_tokens.append(token)
            last_was_operand = True
        else:
            if streak:
                raise InvalidOperatorSequence(f"Invalid sequence of operators near {streak + [token]}")
            fixed_tokens.append(token)
            last_was_operand = False

    if streak:
        raise InvalidOperatorsTrail(f"Trailing operator streak: {streak}")

    return fixed_tokens


def infix_to_postfix(fixed_tokens, operators_dic):
    postfix = []
    stack = []
    index = 0
    precedence = {symbol: operators_dic[symbol].getPriority() for symbol in operators_dic}

    for token in fixed_tokens:
        if is_operand(token):
            postfix.append(token)

        elif token in operators_dic:
            while (
                    stack and stack[-1] in operators_dic and
                    attach_unary_minus(precedence, stack, token)
            ):
                postfix.append(stack.pop())
            stack.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            if not postfix:
                raise InvalidParenthesesUse(f"You need to open a: ( for the ) at index {index}")
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        index += 1

    while stack:
        postfix.append(stack.pop())

    return postfix


def evaluate_postfix(postfix, operators_dic):
    stack = []
    for token in postfix:
        if is_operand(token):
            stack.append(float(token))
        elif token in operators_dic:
            operator = operators_dic[token]
            if operator.getPosition() in ["left", "right"]:
                val = stack.pop()
                stack.append(operator.operate(val))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operator.operate(a, b))
    return stack.pop()
