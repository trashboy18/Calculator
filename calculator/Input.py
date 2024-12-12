from Calculate import calculate


def main():
    print("Welcome to the ultimate calculator!\n")
    while True:
        expression = input("enter you mathematical expression here:\n")
        calculate(expression)

if __name__ == "__main__":
    main()


