# Your solution to Exercise 23
sum = 0
num = 1
count = 0
while num != 0:
    num = int(input("Enter a number you want to add:  "))
    sum += num 
    count += 1
avg = sum/(count-1)
print(avg)