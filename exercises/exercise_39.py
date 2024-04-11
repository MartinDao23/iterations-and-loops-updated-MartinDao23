# Your solution to Exercise 39
x = int(input("Enter a number"))
x = str(abs(x))
sum = 0
for i in range(len(x)):
    sum += int(x[i])
print(sum)