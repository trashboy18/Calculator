from operators import Add, Decrease, Multiply, Divide, Power, Mod, Maximum, Minimum, Average, Tilde, Factorial


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
}

def calculate(expression):
    operators_symbols = operators_dic.keys()
    tokens_arr = tokenize(expression, operators_symbols)
    print(tokens_arr)

def tokenize(expression, operators_symbols):
    tokens = []
    index = 0
    current_num = ''
    while index < len(expression):
        char = expression[index]
        if char.isdigit() or char == '.':
            current_num += char
            index += 1
        elif char in operators_symbols or char in "()":
            if current_num != '':
                tokens.append(current_num)
                current_num = ''
            if char == '-' and (
                index == 0 or expression[index - 1] in operators_symbols or expression[index - 1] == '('
            ):
                current_num = char
                index += 1
            else:
                tokens.append(char)
                index += 1
        else:
            raise ValueError(f"The char {char} is not valid in this calculator.")
    if current_num != '':
        tokens.append(current_num)
    print("Finished\n")
    return tokens
