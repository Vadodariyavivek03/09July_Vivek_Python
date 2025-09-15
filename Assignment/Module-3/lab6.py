# Write a Python program to create a file and write a string into it.

import os

os.chdir("Text_Data")

x = open("my_file1.txt", "a")

my_str = input("Enter your string :: ")

x.write(f"{my_str}")

x.close()

print("Data Write Successfully...!!")