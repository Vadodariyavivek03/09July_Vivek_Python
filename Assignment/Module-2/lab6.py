# Write a Python program to remove elements from a list using pop() and remove().

my_list = ['English', 'Math', 21, 89, 'Science', 3.14, True, ['History', 42], 15.36]

print(my_list)

my_list.pop(2)  # Remove at index 2
print(my_list)

my_list.remove('Math')  # Remove element 'Math'
print(my_list)

my_list.pop()  # Remove the last element
print(my_list)