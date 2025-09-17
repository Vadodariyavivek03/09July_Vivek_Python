# Write a Python program to print custom exceptions.

try:
    n = int(input("Enter a number : "))
    sum_of_pow = 0
    power = len(str(n))

    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_pow += digit ** power
        temp //= 10

    if n != sum_of_pow:
        raise Exception("No!! It's not an Armstrong number...") 
    print("Yes!! It is an Armstrong number...")

except Exception as e:
    print("Error ::",e)

