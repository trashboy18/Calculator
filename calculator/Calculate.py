from Exceptions import CalculatorException
from operators import *
from Conversions import *
from colorama import Fore,Style
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

    expression = expression.replace(" ", "").replace("\t", "")

    try:
        tokens_arr = tokenize(expression, operators_dic)
        check_validity(tokens_arr,operators_dic)
        fixed_tokens = normalize_tokens(tokens_arr)
        postfix = infix_to_postfix(fixed_tokens,operators_dic)

        solution = evaluate_postfix(postfix,operators_dic)
        if (float(solution)).is_integer():
            print(f"{Fore.GREEN}The answer is: {int(solution)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}The answer is: {solution}{Style.RESET_ALL}")
    except CalculatorException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        print("Please try again.")


    except Exception as e:
        print(f"{Fore.CYAN}Error: somehow, you found an error that I couldnt think of. well done.{Style.RESET_ALL}")
        print("try again if you'd like.")
