# Your solution to Exercise 27
n = int(input("Enter a number"))
divi = 1
sum = 0
for i in range(1,n+1):
    if (i%2) == 0:
        sum = sum + (4/divi)
    else:
        sum = sum - (4/divi)
    divi += 2
print(abs(sum))