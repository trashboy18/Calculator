from operators import Hashtag,UnaryMinus,Add, Decrease, Multiply, Divide, Power, Mod, Maximum, Minimum, Average, Tilde, Factorial
from Conversions import tokenize, infix_to_postfix, evaluate_postfix

operators_dic = {
    '+': Add(),
    '-': Decrease(),
    '*': Multiply(),
    '/': Divide(),
    '^': Power(),
    '%': Mod(),
    '$': Maximum(),
    '&': Minimum(),
    '@': Average(),
    '~': Tilde(),
    '!': Factorial(),
    '#':Hashtag(),
    'unary_minus':UnaryMinus()
}
def calculate(expression):
    expression = expression.replace(" ", "")
    tokens_arr = tokenize(expression, operators_dic)
    print(tokens_arr)
    postfix = infix_to_postfix(tokens_arr,operators_dic)
    print(postfix)
    solution = evaluate_postfix(postfix,operators_dic)
    print(f"the answer is:{solution}")
