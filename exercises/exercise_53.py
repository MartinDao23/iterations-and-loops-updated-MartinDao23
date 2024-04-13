# Your solution to Exercise 53
a = int(input("Enter a number"))
b= int(input("Enter a number"))
a = (a+1) * (a%2 == 1) 
for i in range (a,b+2,2):
    print(i)