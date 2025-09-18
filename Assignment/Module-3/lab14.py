# Write a Python program to create a class and access its properties using an object.

from random import *

class My_Info:

    Id = randint(1111, 9999)
    name = "Vivek"
    course = "Python"
    age = 21
    city = "Rajkot"

    def vote_age(self):
        if self.age >= 18:
            print(f"\n{self.name} is eligible to vote.\n")
        else:
            print(f"\n{self.name} is not eligible to vote.\n")

stu = My_Info()

print("\nId ::",stu.Id)
print("Name ::",stu.name)
print("Course ::",stu.course)
print("Age ::",stu.age)
print("City ::",stu.city)

stu.vote_age()
