# Your solution to Exercise 25
target_distance = int(input("What is the total distance?"))
distance = int(input("What distance is covered on day 1?"))
days = 1
while distance < target_distance:
    distance = distance*1.1
    days += 1
print(round(distance,2), "km,", days, "days")