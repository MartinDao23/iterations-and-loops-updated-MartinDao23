# Your solution to Exercise 37
a = int(input("Enter a number"))
b = int(input("Enter a number"))
count = -1
while a >= 0:
    a -= b
    count += 1
remainder = a + b
print(count)
print(remainder)