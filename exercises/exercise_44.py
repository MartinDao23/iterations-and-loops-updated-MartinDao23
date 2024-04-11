# Your solution to Exercise 44
x = int(input("Enter a number"))
arr = []
while x != 0:
    arr.append(x)
    x = int(input("Enter a number"))
for i in range(len(arr)):
    if arr[i] == max(arr):
        print(i)