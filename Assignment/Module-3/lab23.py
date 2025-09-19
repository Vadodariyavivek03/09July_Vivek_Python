# Write Python programs to demonstrate method overloading and method overriding.

# Method OverLoading

class Book:

    def get_data(self, id, name):
        print("Id ::",id)
        print("Name ::",name)

    def get_data(self, author, publisher, pages):
        print("Author ::",author)
        print("Publisher ::",publisher)
        print("Pages ::",pages)


b1 = Book()

# b1.get_data(124, "Atomic Habits")
b1.get_data("James Clear", "Avery", 320)
