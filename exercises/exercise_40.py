# Your solution to Exercise 40
n = int(input("Enter a number"))
y = 1
x = 0
z=1
while z < n:
    print(z, " ", end = "")
    z = x + y
    x = y
    y = z