# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# single-level inheritance

class Vehicle:

    brand : str
    fuel : str

    def get_data(self):
        self.brand = input("Enter Vehicle Brand Name :: ")
        self.fuel = input("Enter Your Vehicle Fuel Type :: ")

class Car(Vehicle):

    def print_data(self):
        print("Brand ::",self.brand)
        print("Fuel Type ::",self.fuel)

c1 = Car()

c1.get_data()
c1.print_data()

