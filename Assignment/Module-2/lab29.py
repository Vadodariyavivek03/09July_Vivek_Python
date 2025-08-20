# Write a Python program to create a lambda function with two expressions.

digit = lambda n : "even" if n%2 == 0 else "odd"

print(digit(8))
print(digit(5))


# ---------------------------------- #

digit = lambda a,b : (a+b, a*b)

ans = digit(6,3)

print("Sum :",ans[0])
print("Production :",ans[1])