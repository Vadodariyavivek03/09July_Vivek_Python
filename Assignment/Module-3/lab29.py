# Write a Python program to match a word in a string using re.match().

import re

my_str = input("Enter String :: ")

x = re.match("Python", my_str)

print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")