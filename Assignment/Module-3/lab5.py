# Write a Python program to open a file in write mode, write some text, and then close it.

import os

os.chdir("Text_Data")

x = open("temp.txt", "w")

id = int(input("Enter an ID : "))
name = input("Enter a Name : ")
age = int(input("Enter an Age : "))
city = input("Enter a City : ")

x.write(f"ID : {id}\n")
x.write(f"Name : {name}\n")
x.write(f"Age : {age}\n")
x.write(f"City : {city}\n")

x.close()

print("Data Write Successfully...!!")