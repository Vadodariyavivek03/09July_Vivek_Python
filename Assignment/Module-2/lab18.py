# Write a Python program to access values using dictionary keys.

my_data = {
            "id" : 101,
            "name" : "Vivek",
            "age" : 21,
            "subject" : "Python",
            "mobile" : 1234567890,
            "city" : "Rajkot",
            "country" : "India"
          }

print(my_data)

# ----------------------------------------- #

for i in my_data.values():
    print(i)

# ----------------------------------------- #

'''for i in my_data.keys():
    print(i)'''

# ----------------------------------------- #

for i,j in my_data.items():
    print(f"{i} ---> {j}")