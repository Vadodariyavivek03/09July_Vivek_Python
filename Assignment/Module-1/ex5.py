n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 != 0 and n2 != 0:

    if n1 > n2 :
        print("The Multiplication is: ", n1 * n2)
    else:
        print("The Sum is: ", n1 + n2)

else:
    print("Numbers are zero, Invalid.")