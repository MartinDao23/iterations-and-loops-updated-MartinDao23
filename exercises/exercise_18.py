# Your solution to Exercise 18
n = int(input("How many numbers will be entered  "))
sum = 0
for i in range(n):
    number = int(input("Enter a number  "))
    sum += number
print(sum)