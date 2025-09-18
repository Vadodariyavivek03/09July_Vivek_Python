# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# multilevel inheritance

class Book:

    def get_data_1(self):
         self.title = input("Enter book title :: ")
         self.publisher = input("Enter publisher name :: ")

class Author(Book):

    def get_data_2(self):
        self.name = input("Enter author name :: ")

class Info(Author):

    def get_data_3(self):
        self.pages = int(input("Enter number of pages :: "))
        self.price = float(input("Enter book price :: "))

    def print_data(self):
        print("\n-----Book Information-----")
        print("Title ::",self.title)
        print("Publisher ::",self.publisher)
        print("Author ::",self.name)
        print("Pages ::",self.pages)
        print("Price :: Rs.",self.price)
        print()

b1 = Info()

b1.get_data_1()
b1.get_data_2()
b1.get_data_3()
b1.print_data()