# Your solution to Exercise 8
n = int(input("What number do you want to print until: "))
for i in range (1, n+1):
    if i%2 == 0:
        print(i)
    else:
        continue 