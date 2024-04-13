# Your solution to Exercise 43
x = int(input("Enter a number"))
arr = []
while x != 0:
    arr.append(x)
    x = int(input("Enter a number"))
arr.sort()
print(arr)
print(arr[len(arr)-2])