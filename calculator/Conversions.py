
def tokenize(expression, operators_dic):
    tokens = []
    index = 0
    current_num = ''
    operator_symbols = operators_dic.keys()
    while index < len(expression):
        char = expression[index]

        if char.isdigit() or char == '.':
            current_num += char
            index += 1
        elif char in operator_symbols or char in "()":
            if current_num != '':
                tokens.append(current_num)
                current_num = ''

            if char == '-':
                # Determine if it's unary or binary
                if (index == 0 or (tokens[-1] in operator_symbols and
                                   operators_dic[tokens[-1]].getPosition() != "right")
                        or tokens[-1] == '('):
                    tokens.append('unary_minus')  # It's unary minus
                else:
                    tokens.append('-')
                index += 1
            else:
                tokens.append(char)
                index += 1
        else:
            raise ValueError(f"The character '{char}' is not valid in this calculator.")

    if current_num != '':
        tokens.append(current_num)

    return tokens

def infix_to_postfix(tokens, operators_dic):
    postfix = []
    stack = []
    precedence = {symbol: operators_dic[symbol].getPriority() for symbol in operators_dic}

    for token in tokens:
        if token.isdigit() or '.' in token:  # Numbers go directly to the output
            postfix.append(token)
        elif token in operators_dic:  # Operators
            operator = operators_dic[token]
            if operator.getPosition() in ["left","right"]:  # Handle unary operators
                stack.append(token)
            else:  # Handle binary operators
                while (stack and stack[-1] != '(' and
                       precedence[stack[-1]] >= precedence[token]):
                    postfix.append(stack.pop())
                stack.append(token)
        elif token == '(':  # Opening parenthesis
            stack.append(token)
        elif token == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '('

    # Pop remaining operators in the stack
    while stack:
        postfix.append(stack.pop())

    return postfix


def evaluate_postfix(postfix, operators_dic):
    stack = []

    for token in postfix:
        if token.isdigit() or '.' in token:  # Push numbers onto the stack
            stack.append(float(token))
        elif token in operators_dic:  # Operators
            operator = operators_dic[token]
            if operator.getPosition() in ["left","right"]:  # Handle unary operators
                stack.append(operator.operate(stack.pop()))
            else:  # Handle binary operators
                b = stack.pop()
                a = stack.pop()
                stack.append(operator.operate(a, b))

    return stack.pop()




