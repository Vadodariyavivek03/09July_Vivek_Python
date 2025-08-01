# Write a Python program to create a tuple with multiple data types.

items = (False, 'Watch', 'Book', 'Shoes', 24, 89.25, 'Pen', 'Smartwatch', 54, 3.14, True, 'Laptop', 'Bag')

print(items)

for i in items:
    print(f"{i} --> {type(i)}") 