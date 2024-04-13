# Your solution to Exercise 52
a = int(input("Enter a number"))
b= int(input("Enter a number"))
a = (a-1) * (a%2 == 0)
for i in range (a,b,-2):
    print(i)