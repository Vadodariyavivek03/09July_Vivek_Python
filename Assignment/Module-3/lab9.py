# Write a Python program to check the current position of the file cursor using tell().

import os

os.chdir("Text_Data")

x = open("my_file3.txt", "w")

my_str = "Python is a powerful programming language that is easy to learn. It is widely used in web development."

x.write(f"{my_str}")

print("\nData Print Successfully...!!\n")

# ---------------------------------------------- #

x = open("my_file3.txt", "r")

print("Initial cursor position : ",x.tell())
print(f"{"-" * 50}") 

obj = x.read(3)
print("Cursor position after reading 3 chars:", x.tell())
print("String ::",obj)
print(f"{"-" * 50}") 
 
obj = x.read(8)
print("Cursor position after reading 8 chars:", x.tell())
print("String ::",obj)
print(f"{"-" * 50}") 

obj = x.read(15)
print("Cursor position after reading 15 chars:", x.tell())
print("String ::",obj)
print(f"{"-" * 50}") 

