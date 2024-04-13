# Your solution to Exercise 35
digits = int(input("Enter a number"))
for i in range (10**(digits-1),(10**digits)):
    if (i%2) == 1:
        print(i)