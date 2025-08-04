# Write a Python program to count how many times each character appears in a string.

my_str = input("Enter your string : ")

my_data = {}

for i in my_str:
    if i in my_data:
        my_data[i] += 1
    else:
        my_data[i] = 1

for i,j in my_data.items():
    if i == " ":
        print("[space] :",j)
    else:
        print(f"{i} ---> {j}")