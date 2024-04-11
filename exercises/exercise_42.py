# Your solution to Exercise 42
x = int(input("Enter a number"))
count = -1
while x != 0:
    y = int(input("Enter a number"))
    if x > y:
        count += 1
    x = y
print(count)