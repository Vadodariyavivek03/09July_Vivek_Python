FullName = input("Please enter your name : ")
DOB = input("Please enter your date of birth : ")
Address = input("Please enter your address : ")
Mobile = int(input("Please enter your mobile no : "))  #input() always return str datatype.

print("My name is : ",FullName)
print("Date of Birth : ",DOB)
print("Address : ",Address)
print("Mobile : ",Mobile)

print(type(FullName))
print(type(Mobile))