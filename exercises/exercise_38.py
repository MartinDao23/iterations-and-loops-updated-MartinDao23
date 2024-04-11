# Your solution to Exercise 38
x = input("Enter a number")
max = 0
min = 10
for i in range(len(x)):
    if int(x[i]) > max:
        max = int(x[i])
    if int(x[i]) < min:
        min = int(x[i])
ans = "True" if ((max-min)%2 == 0) else "False"
print(ans)