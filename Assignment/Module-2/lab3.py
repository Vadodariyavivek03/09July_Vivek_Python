# Write a Python program to create a list of multiple data type elements. --- dynamic input

my_list = []

n = int(input("Enter how many elements : "))

for i in range(n):
    x = input(f"Enter element {i+1} : ")

    if x.isdigit():                                        # check for int.
        my_list.append(int(x))

    elif '.' in x and x.replace('.', '', 1).isdigit():     # check for float.
        my_list.append(float(x))

    elif x.lower() in ['true', 'false']:                   # check for boolean.
        my_list.append(x.lower() == 'true')
        
    else:                                                  # string.
        my_list.append(x)    

print(my_list)

for i in my_list:
    print(f"{i} --> {type(i)}")