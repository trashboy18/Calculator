from Calculate import calculate


def main():
    print("Welcome to the ultimate calculator!\n")
    expression = input("enter you mathematical expression here:\n")
    expression = expression.replace(" ", "")
    calculate(expression)

if __name__ == "__main__":
    main()


