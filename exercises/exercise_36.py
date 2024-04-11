# Your solution to Exercise 36
a = int(input("Enter a number"))
b = int(input("Enter a number"))
x = a % b
while x != 0:
    a = b
    b = x
    x = a % b
print(b)