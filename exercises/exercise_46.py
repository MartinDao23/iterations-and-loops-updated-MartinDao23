# Your solution to Exercise 46
d = input("Enter a number")
n = input("Enter a number")
for i in range (len(n)-1,-1, -1):
    if n[i] == d:
        print(len(n)-i)
        break