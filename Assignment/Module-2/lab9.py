# Write a Python program to insert elements into an empty list using a for loop and append().

fruits = []

n = int(input("Enter how many fruits you want to add : "))

for i in range(n):
    x = input(f"Enter fruit {i+1} : ")
    fruits.append(x)
    
print(fruits)