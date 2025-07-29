# Write a Python program that manipulates and prints strings using various string methods.

para = "36458941thatistheisoftheperson"
para1 = "7548961239"
para2 = "Vivek"
para3 = "Vivek H. Vadodariya"

# this all method returns boolean value.

print(para.isalnum())    #  alphanumeric (letters and numbers).

print(para1.isnumeric()) #  numeric.

print(para.isalpha())    #  alphabetic.

print(para1.isdigit())   #  digits.

print(para2.islower())

print(para.isupper())

print(para3.isspace())   # This will return true if the string contains only whitespace characters.

print(para3.istitle())