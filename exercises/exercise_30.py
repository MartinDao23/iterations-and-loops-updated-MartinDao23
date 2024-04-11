# Your solution to Exercise 30
t = int(input("Enter a number"))
cells = 1
for i in range(t//3):
    cells *= 2
print(cells)