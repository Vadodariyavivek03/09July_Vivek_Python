FullName = input("Enter your full name: ")
if not FullName.isalpha():
    print("Please enter a valid name containing only letters.")  
    exit()

Mobile = input("Enter your mobile number: ")
if not (Mobile.isdigit() and len(Mobile) == 10):
    print("Please enter a valid 10-digit mobile number.")
    exit()

Email = input("Enter your email address: ")
if not (Email.islower() and '@' in Email):
    print("Please enter a valid email address in lowercase with '@' symbol.")
    exit()

Password = input("Enter your password: ")
if not (Password.isalnum() and len(Password) < 8):
    print("Please enter a valid password containing at least 8 alphanumeric characters.")
    exit()

ConfirmPassword = input("Confirm your password: ")
if Password != ConfirmPassword and not ConfirmPassword.isalnum():
    print("Passwords do not match or are not valid.")
    exit()

print("**********Registration successful**********")