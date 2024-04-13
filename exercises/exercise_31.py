# Your solution to Exercise 31
days = int(input("Enter the number of days"))
lowest_temp = 10000000
for i in range (days):
    temp = int(input("What is the temp?"))
    lowest_temp = temp if (temp < lowest_temp) else lowest_temp
print(lowest_temp)
print("yes") if lowest_temp < -15 else ""