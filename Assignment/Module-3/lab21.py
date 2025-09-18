#  Write a Python program to show hybrid inheritance.

class Machine:

    def display(self):
        print("This is a machine...!!")

class Vehicle(Machine):

    def get_data(self):
        print("This is a vehicle...!!")

class Car(Vehicle):

    def car_data(self):
        print("This is a car...!!")

class Bike(Vehicle):

    def bike_data(self):
        print("This is a bike...!!")

class E_Vehicle(Car, Bike):

    def e_data(self):
        print("This is an electrical vehicle...!!")

obj = E_Vehicle()

obj.display()
obj.get_data()
obj.car_data()
obj.bike_data()
obj.e_data()
