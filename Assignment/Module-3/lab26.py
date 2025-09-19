# Method Overriding

class School_Data:

    def get_data(self, id, name):
        print("Id ::",id)
        print("Name ::",name)

class Student_Info(School_Data):

    def get_data(self, id, name):
        return super().get_data(id, name)
    
class Faculty_Info(School_Data):

    def get_data(self, id, name):
        return super().get_data(id, name)
    
sd = School_Data()
sd.get_data(111, "Vivek")

si = Student_Info()
si.get_data(121, "Meet")

fi = Faculty_Info()
fi.get_data(2211, "Kashyap")