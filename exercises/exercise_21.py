# Your solution to Exercise 21
b = int(input("Enter a number"))
sum = 0
fact = 1
for i in range (1,b+1):
    for x in range (1,i+1):
        fact = fact*x
    sum += fact
    fact = 1
print(sum)