age = int(input("Enter your age : "))

if age < 18 :
    print("You are not eligible to vote!!!")
else:
    if age >= 18 and age < 60:
        print("You are eligible to vote!!!")
    else:
        print("You are a senior citizen person and will be given special care to vote.")