import pytest
from Exceptions import *
from operators import *
from Conversions import (
    tokenize,
    normalize_tokens,
    infix_to_postfix,
    evaluate_postfix,
    check_validity,
)

# Operators dictionary for testing
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
    '#': Hashtag(),
    'unary_minus': UnaryMinus(),
}

# Test invalid syntax
@pytest.mark.parametrize("expression,exception", [
    ("2*^3", InvalidOperatorPlacement),
    ("3++4", InvalidOperatorPlacement),
    ("10(/2)", InvalidParenthesesUse),
    ("4!-", InvalidOperatorPlacement),
])
def test_invalid_syntax_expressions(expression, exception):
    with pytest.raises(exception):
        tokens = tokenize(expression, operators_dic)
        check_validity(tokens, operators_dic)
        normalized_tokens = normalize_tokens(tokens)
        infix_to_postfix(normalized_tokens, operators_dic)

# Test gibberish
@pytest.mark.parametrize("expression,exception", [
    ("asdfgh", InvalidCharException),
    ("!!!", InvalidOperatorPlacement),
    ("2&hello", InvalidCharException),
    ("#3%5&", InvalidOperatorPlacement),
    ("@invalid", InvalidCharException),
])
def test_gibberish_expressions(expression, exception):
    with pytest.raises(exception):
        tokens = tokenize(expression, operators_dic)
        check_validity(tokens, operators_dic)
        normalized_tokens = normalize_tokens(tokens)
        infix_to_postfix(normalized_tokens, operators_dic)

# Test empty and whitespace-only expressions
@pytest.mark.parametrize("expression,exception", [
    ("", InvalidEmptyExpression),
    (" ", InvalidEmptyExpression),
    ("\t\t", InvalidEmptyExpression),
    ("\n", InvalidEmptyExpression),
])
def test_empty_expressions(expression, exception):
    with pytest.raises(exception):
        tokens = tokenize(expression, operators_dic)

# Test invalid use of parentheses
@pytest.mark.parametrize("expression,exception", [
    ("(2+3", InvalidParenthesesUse),
    ("2+3)", InvalidParenthesesUse),
    ("((2+3)", InvalidParenthesesUse),
    ("2+(3+4))", InvalidParenthesesUse),
    ("(2*(3+4)", InvalidParenthesesUse),
])
def test_invalid_parentheses(expression, exception):
    with pytest.raises(exception):
        tokens = tokenize(expression, operators_dic)
        check_validity(tokens, operators_dic)
        normalized_tokens = normalize_tokens(tokens)
        infix_to_postfix(normalized_tokens, operators_dic)

# Test edge cases
@pytest.mark.parametrize("expression,expected_output", [
    ("1+0", 1),
    ("0*1000", 0),
    ("~(~(~(~1)))", 1),
    ("-(-2^2)", 4),
    ("~(2*3)-(~2)", -4),
])
def test_edge_cases(expression, expected_output):
    tokens = tokenize(expression, operators_dic)
    check_validity(tokens, operators_dic)
    normalized_tokens = normalize_tokens(tokens)
    postfix = infix_to_postfix(normalized_tokens, operators_dic)
    solution = evaluate_postfix(postfix, operators_dic)
    assert solution == expected_output
