HELP_TEXT = """
Welcome to the advanced calculator! Here's everything you need to know about how it works:

Operators and Their Functions:
1. '+' (Precedence: 1, Position: Middle) - Adds two numbers.
2. '-' (Precedence: 1, Position: Middle) - Subtracts one number from another.
3. '*' (Precedence: 2, Position: Middle) - Multiplies two numbers.
4. '/' (Precedence: 2, Position: Middle) - Divides one number by another.
5. 'U-' (Precedence: 2.5, Position: Left) - Unary minus; negates a number.
6. '^' (Precedence: 3, Position: Middle) - Raises one number to the power of another.
7. '%' (Precedence: 4, Position: Middle) - Calculates the remainder of division.
8. '&' (Precedence: 5, Position: Middle) - Finds the smaller of two numbers.
9. '$' (Precedence: 5, Position: Middle) - Finds the larger of two numbers.
10. '@' (Precedence: 5, Position: Middle) - Calculates the average of two numbers.
11. '!' (Precedence: 6, Position: Right) - Calculates the factorial of a single, non-negative number.
12. '~' (Precedence: 6, Position: Left) - Negates a number.
13. '#' (Precedence: 6, Position: Left) - Another negation operator (equivalent to '~').

Key Features:
- The calculator ensures precedence and associativity rules are strictly followed.
- Complex expressions with multiple operators and parentheses are fully supported.
- Error handling prevents crashes: Invalid inputs, unbalanced parentheses, or improper operator use are detected and reported.
- Supports both integers and floating-point numbers.

Usage Instructions:
1. Enter any valid mathematical expression to calculate its result.
2. Type `stop` to exit the program.
3. Type `-h` at any time to see this help menu.

Error Handling:
- Common mistakes like invalid characters, unsupported syntax, or missing parentheses will prompt an error message and allow you to retry.
- Trailing operators, unsupported sequences, or invalid factorial inputs will also trigger specific error messages.

Testing and Validation:
This calculator has built-in tests to ensure accurate functionality and proper error handling. If you're a developer, you can run these tests using `pytest` in your terminal.

Enjoy using the calculator for your mathematical needs!
"""
