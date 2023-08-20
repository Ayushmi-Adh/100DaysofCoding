# Calculator
import os
from art import logo3

print(logo3)


# ADDITION:
def add(n1, n2):
    return n1 + n2


# SUBTRACTION:
def subtract(n1, n2):
    return n1 - n2


# MULTIPLICATION:
def multiply(n1, n2):
    return n1 * n2


# DIVISION:
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    continue_ = True
    num1 = float(input("Enter the first number: "))

    for sign in operations:
        print(sign)
    while continue_:
        operation_symbol = input("Pick an operation from the lines above: ")

        num2 = float(input("Enter the second number: "))

        calculations = operations[operation_symbol]

        answer = calculations(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_or_not = input(
            f"Type 'yes' if you want to continue with {answer} else type 'no' to start new calculations: ").lower()

        if continue_or_not == "yes":
            num1 = answer
        else:
            continue_ = False
            os.system('cls')
            calculator()


calculator()
