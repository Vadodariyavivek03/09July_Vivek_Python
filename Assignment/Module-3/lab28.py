# Write a Python program to search for a word in a string using re.search().

import re

my_str = input("Enter String :: ")

x = re.search("Hello", my_str)

print(x)

if x:
    print("Match Successfully..!!" )
else:
    print("Error..!!")