#  Print this pattern using nested for loop.

# n = int(input("Enter the number of rows: "))

n = 5

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
      
             