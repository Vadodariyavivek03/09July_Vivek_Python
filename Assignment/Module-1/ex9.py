sign = input("Enter a sign (+, -, *, /): ")

if (sign == '+'or sign == '-' or sign == '*' or sign == '/'):

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if sign == '+':
        print("Result:", num1 + num2)       
    elif sign == '-':
        print("Result:", num1 - num2)
    elif sign == '*':
        print("Result:", num1 * num2)
    elif sign == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid sign. Please enter one of +, -, *, /.")