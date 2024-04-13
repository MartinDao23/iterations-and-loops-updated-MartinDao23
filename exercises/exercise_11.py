# Your solution to Exercise 11
limit = int(input("What is the limit: "))
sum = 0
for i in range(1, limit+1):
    fraction = i/(i+1)
    sum += fraction
sum = round(sum, 2)
print(sum)