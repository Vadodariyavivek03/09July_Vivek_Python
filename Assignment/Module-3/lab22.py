# Write a Python program to demonstrate the use of super() in inheritance.

class Vehicle:

    def display_info(self):
        print("This is a vehicle data....!!")

class Car(Vehicle):

    def car_data(self):

        super().display_info()
        print("This is a car data....!!")

c1 = Car()

c1.car_data()
