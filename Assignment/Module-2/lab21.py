# Write a Python program to update a value at a particular key in a dictionary. 

my_data = {
            "id" : 101,
            "name" : "Vivek",
            "age" : 21,
            "subject" : "Python",
            "mobile" : 1234567890,
            "city" : "Rajkot",
            "country" : "India"
          }

key = input("Enter key to update : ")

for i in my_data:
    if i == key:
        value = input(f"Enter new value for {key} : ")
        my_data[i] = value
        break    # this is use for stop loop if condition satisfied...because without break else part is print many(range) time.                                           
else:
    print("Key is not found!!!")

print(my_data)