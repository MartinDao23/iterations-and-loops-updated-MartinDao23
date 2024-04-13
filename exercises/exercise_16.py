# Your solution to Exercise 16
limit = int(input("What do you want to print untill: "))
for i in range(1, limit+1):
    print(" "*(limit-i) + "#"*i)