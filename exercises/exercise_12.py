# Your solution to Exercise 12
limit = int(input("What is the limit: "))
sum = 0
for i in range(100, 1000):
    if i % limit == 0:
        sum += i
    else:
        continue
print(sum)