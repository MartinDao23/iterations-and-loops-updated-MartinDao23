# Your solution to Exercise 24
x = 1
count = 0
while x != 0:
    x = int(input("Enter a number"))
    if (x%2) == 0 and x != 0:
        count += 1
print(count)