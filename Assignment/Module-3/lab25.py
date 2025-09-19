# Method Overloading

class Stud_Data:

    def get_data(self, id):
        print("Id ::",id)
        
    def get_data(self, name, age, city):
        print("Name ::",name)
        print("Age ::",age)
        print("City ::",city)

    def get_data(self, sub):
        print("Subject ::",sub)

obj = Stud_Data()

# obj.get_data(101)
# obj.get_data("Vivek", 21, "Rajkot")
obj.get_data("Python")
obj.get_data(111)

