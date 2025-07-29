# Write a Python program that manipulates and prints strings using various string methods.

para = "36458941thatistheisoftheperson"
para1 = "7548961239"
para2 = "Vivek"
para3 = "Vivek H. Vadodariya"

# this all method returns boolean value.

print(para.isalnum())    # It checks if all characters in the string are alphanumeric (letters and numbers).

print(para1.isnumeric()) # It checks if all characters in the string are numeric.

print(para.isalpha())    # It checks if all characters in the string are alphabetic.

print(para1.isdigit())   # It checks if all characters in the string are digits.

print(para2.islower())

print(para.isupper())

print(para3.isspace())   # This will return true if the string contains only whitespace characters, which it does not.

print(para3.istitle())