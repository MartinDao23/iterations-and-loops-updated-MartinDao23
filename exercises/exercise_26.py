# Your solution to Exercise 26
n = int(input("Enter a number"))
count = 0
for i in range (100,1000):
    ones = i%10
    tens = (i//10)%10
    hundreds = i//100
    if (ones + tens + hundreds) == n:
        count += 1
print(count)