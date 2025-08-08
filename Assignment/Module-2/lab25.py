# Write a Python program to create a calculator using functions.

def Add(n1,n2):
    print("Addition : ",n1+n2)

def Sub(n1,n2):
    print("Substraction : ",n1-n2)

def Mul(n1,n2):
    print("Multiplication : ",n1*n2)

def Div(n1,n2):
    print("Division : ",n1/n2)

sign = input("Enter a sign (+, -, *, /): ")

if (sign == '+' or sign == '-' or sign == '*' or sign == '/'):

    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))

    if sign == '+':
        Add(n1,n2)
    elif sign == '-':
        Sub(n1,n2)
    elif sign == '*':
        Mul(n1,n2)
    elif sign == '/':
        if n2 != 0:
            Div(n1,n2)
        else:
            print("Error: Division by zero is not allowed.")
            
else:
    print("Enter valid sign.........!")

