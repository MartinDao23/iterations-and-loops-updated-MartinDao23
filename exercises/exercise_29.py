# Your solution to Exercise 29
a = int(input("Enter a number"))
sum = a
a_square_sum = a**2
while sum != 0:
    a = int(input("Enter a number"))
    sum += a
    a_square_sum += a**2
print(a_square_sum//2)