'''
Jianzhong Liu
CS 5002, Spring 2022
Lab 2 -- 2.Arithmetic

This program is a simple arithmetic program
that we can input 2 float or integer number
and choose an operation to output arithmetic
result
'''


def main():
    number1 = float(input("Input first number: "))
    number2 = float(input("Input second number: "))
    operator = str(input("Input operator (+, -, *, /): "))
    if operator == "+":
        print(number1, operator, number2, "=", number1 + number2)
    elif operator == "-":
        print(number1, operator, number2, "=", number1 - number2)
    elif operator == "*":
        print(number1, operator, number2, "=", number1 * number2)
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
            print(number1, operator, number2, "=", result)
        else:
            print(number1, operator, number2, "=", "NaN")
    else:
        print("Invalid operator. Please use +,-,*,/.")



if __name__ == '__main__':
    main()


