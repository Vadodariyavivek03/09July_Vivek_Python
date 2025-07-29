# Write a Python program that manipulates and prints strings using various string methods.

mystr = "Hello! python is interpred, object oriented and high level programming language."

print(mystr) 

print(len(mystr))

print(mystr.count("e"))

print(mystr.strip())      # Remove whitespace from start and end.

print(mystr.lower())

print(mystr.upper())

print(mystr.replace("python", "Java"))  # Replace "python" with "Java"

print(mystr.split())  

print(mystr.capitalize()) # Capitalize the first letter of the string

print(mystr.title())      # Capitalize the first letter of each word

print(mystr.casefold())   # Convert the string to lowercase for case-insensitive comparisons.

print(mystr.startswith("Hello"))  # Check if the string starts with "Hello" and return boolean value.

print(mystr.endswith("Python"))   # Check if the string ends with "Python" and return boolean value.

print(mystr.find("python"))       # Find the first occurrence of "python" and return its index, or -1 if not found.

print(mystr.index("object"))