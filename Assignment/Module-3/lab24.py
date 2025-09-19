# Write Python programs to demonstrate method overloading and method overriding.

# Method Overriding

class Bank_Info:

    def acc_open(self, name):
        print(f"{name}... Your General Account Open Successfully...!!")

class Saving_Account(Bank_Info):

    def acc_open(self, name):
        print(f"{name}... Your Saving Account Open Successfully...!!")

class Current_Account(Bank_Info):

    def acc_open(self, name):
        print(f"{name}... Your Current Account Open Successfully...!!")

b1 = Bank_Info()
b1.acc_open("Vivek")

sav = Saving_Account()
sav.acc_open("Meet")

ca = Current_Account()
ca.acc_open("Kashyap")
