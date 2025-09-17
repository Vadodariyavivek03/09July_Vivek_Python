# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    sign = input("Enter a sign (+, -, *, /): ")

    if sign not in ['+', '-', '*', '/']:
        raise ValueError("Error :: Invalid operator!!")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if sign == '+':
        print("Result:", num1 + num2) 

    elif sign == '-':
        print("Result:", num1 - num2)

    elif sign == '*':
        print("Result:", num1 * num2)

    elif sign == '/':
       print("Result:", num1 / num2)

except Exception as e:
    print("Error ::",e)

