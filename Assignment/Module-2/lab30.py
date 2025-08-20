# Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().

from math import *

print(sqrt(49))
print(ceil(5.45))
print(floor(12.85))

#---------------- User Input ------------------#

x = int(input("\nEnter value : "))
print("Sqrt :",sqrt(x))

y = float(input("\nEnter value : "))
print("Ceil :",ceil(y))

z = float(input("\nEnter value : "))
print("Floor :",floor(z))