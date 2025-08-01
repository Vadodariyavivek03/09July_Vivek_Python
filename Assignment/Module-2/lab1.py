# Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.).

my_list = ['English', 'Math', 21, 89, 'Science', 3.14, True, ['History', 42], 15.36]

print(my_list)

for i in my_list:
    print(f"{i} --> {type(i)}")  