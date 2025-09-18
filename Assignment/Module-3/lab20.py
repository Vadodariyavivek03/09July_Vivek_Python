#  Write a Python program to show hierarchical inheritance.

class shape:
    def area(self):
        print("This is area of different shapes,,,,")

class circle(shape):
    def area(self):
        radius = int(input("\nEnter Radius : "))
        area = 3.14 * radius * radius
        print("Area of Circle ::",area)
        print()

class square(shape):
    def area(self):
        side = int(input("Enter Side Value : "))
        area = side * side
        print("Area of Square ::",area)
        print()

class rectangle(shape):
    def area(self):
        length = int(input("Enter Length : "))
        width = int(input("Enter Width : "))
        area = length * width
        print("Area of Rectangle ::",area)
        print()

ci = circle()
sq = square()
rec = rectangle()

ci.area()
sq.area()
rec.area()
