# Your solution to Exercise 19
n = int(input("What number will be divided  "))
for i in range(10, 100):
    n1 = i//10
    n2 = i%10
    if ((n1**2) + (n2**2))%n == 0:
        print(str(i)+" ", end = "")