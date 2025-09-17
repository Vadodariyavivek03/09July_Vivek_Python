# Write a Python program to demonstrate handling multiple exceptions.

import os

os.chdir("Text_Data")

try:

    filename = input("Enter Filename :: ")

    x = open(filename, "r")

    print("File Content ::",x.read(),sep="\n")
    # print(x.read)

# ------------------------------------------------- #

    n1 = int(input("Enter number 1 :: "))
    n2 = int(input("Enter number 2 :: "))

    res = n1 / n2
    print("Result ::",res)

# ------------------------------------------------- #

except FileNotFoundError:
    print("Error :: File not found")
except ZeroDivisionError:
    print("Error :: Division by zero")
except ValueError:
    print("Error :: Invalid input, please enter integers value.")
except Exception as e:
    print("Unexpected error :: ", e)
