# Your solution to Exercise 33
n = int(input("Enter a number"))
for i in range (n):
    print("-1"*i, end = "")
    print("0", end = "")
    print("1"*(n-(i+1)), end = "")
    print("")