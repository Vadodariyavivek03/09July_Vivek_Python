# Write a Python program to find a specific string in the list using a simple for loop and if condition.

list1 = ['apple', 'mango', 'orange', 'banana', 'kiwi', 'grape', 'peach', 'pear', 'cherry', 'watermelon']

search_fruit = 'banana'

for fruit in list1:
    if fruit == search_fruit:
        print(f"Found : {search_fruit}")
        break
    else:
        print(f"{search_fruit} is not found.")

    

