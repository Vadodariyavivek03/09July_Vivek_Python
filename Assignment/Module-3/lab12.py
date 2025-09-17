# Write a Python program to handle file exceptions and use the finally block for closing the file.

import os

os.chdir("Text_Data")

try:
    filename = input("Enter Filename :: ")

    x = open(filename, "r")

    print("Data Read ::",x.read(), sep="\n")

except FileNotFoundError:
    print("Error :: File not found!!")
except Exception as e:
    print("Error ::",e)

finally:
    try:
        x.close()
        print("File Closed Successfully!!")
    except NameError:
            print("Error :: No file to close...")

    
    