# Your solution to Exercise 10
pounds = int(input("What is the mass in pounds"))
for i in range(1, pounds+1):
    kg = i*0.453
    print(f"{i} {kg}")