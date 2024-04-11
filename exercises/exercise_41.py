# Your solution to Exercise 41
n = int(input("Enter a number"))
y = 1
x = 0
z=1
for i in range(n-1):
    z = x + y
    x = y
    y = z
print(z)