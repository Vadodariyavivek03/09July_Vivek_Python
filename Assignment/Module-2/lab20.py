# Write a Python program to merge two lists into one dictionary using a loop.

keys = ['id', 'name', 'age', 'mobile', 'city', 'country']
values = [1001, 'Aansh', 24, 1234567890, 'Surat', 'India']

my_data = {}

for i in range(len(keys)):
     my_data[keys[i]] = values[i]

print(my_data)
