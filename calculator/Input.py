from Calculate import calculate
from colorama import Fore,Style
from Help_text import HELP_TEXT

def main():
    print("Welcome to the ultimate calculator!\n")
    expression = 'stam'

    while expression.upper() != "STOP":
        try:
            expression = input("Enter your mathematical expression here:\n"
                "Type 'stop' to finish, or '-h' for help\n")
            if expression.replace(" ", "").replace("\t", "") == '-h':
                print(f"{Fore.YELLOW}{HELP_TEXT}{Style.RESET_ALL}")
                continue
            calculate(expression)
        except KeyboardInterrupt:
            print(f"{Fore.RED}terminating the program won't make me crash.{Style.RESET_ALL}")
            expression = "stop"
        except EOFError:
            print(f"{Fore.RED} EOF got nothing on me!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()


