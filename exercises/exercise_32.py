# Your solution to Exercise 32
cars = int(input("Enter the number of cars"))
below_30 = 0
highest = 0
lowest = 300
for i in range (cars):
    speed = int(input("How fast was the car going"))
    if speed < 30:
        below_30 += 1
    if speed > highest:
        highest = speed
    if speed < lowest:
        lowest = speed
range = highest - lowest
print(range)
print(below_30)