# Your solution to Exercise 45
x = int(input("Enter a number"))
arr = []
count = 0
while x != 0:
    arr.append(x)
    x = int(input("Enter a number"))
for i in range(len(arr)-1):
    if (arr[i] > 0 and arr[i+1] < 0) or (arr[i] < 0 and arr[i+1] > 0):
        count += 1
print(count)