# Your solution to Exercise 9
a = int(input("Enter a number for the lower limit"))
b = int(input("Enter a number for the higher limit"))
c = int(input("Enter a number for the multiple"))
for i in range(a,b+1):
    if i%c == 0:
        print(i)
    else:
        continue