# Write a Python program to read the contents of a file and print them on the console.

import os 

os.chdir("Text_Data")

x = open("temp.txt", "r")

print(x.read())

# print(x.read(5))

# print(x.readline())

# print(x.readlines())

# print(x.readlines()[1])

# for i in x:
#     print(i)

print("Data Read Successfully...!!\n")