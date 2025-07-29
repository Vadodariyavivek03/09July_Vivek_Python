# Write a Python program to calculate grades based on percentage using if-else ladder.

a = int(input("Enter the mark a : "))
b = int(input("Enter the mark b : "))
c = int(input("Enter the mark c : "))
d = int(input("Enter the mark d : "))


if a >= 40 and b >= 40 and c >= 40 and d >= 40:
      
    avg = a + b + c + d
    print("Total Mark : ",avg)

    PR = avg / 4
    print("Percentage : ",PR)
        
    if PR >= 80:
        print("Grade A")
    elif PR >= 65:
        print("Grade B")
    elif PR >= 50:
        print("Grade C")
    elif PR >= 40:
        print("Grade D")
        
else:
    print("Fail!")