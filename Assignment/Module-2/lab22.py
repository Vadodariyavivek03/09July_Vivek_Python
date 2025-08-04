# Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

my_data = {
            "id" : 101,
            "name" : "Vivek",
            "age" : 21,
            "subject" : "Python",
            "mobile" : 1234567890,
            "city" : "Rajkot",
            "country" : "India"
          }

'''keys = list(my_data.keys())
values = list(my_data.values())'''

keys = my_data.keys()
values = my_data.values()

print("Keys : ",keys)
print("Values : ",values)