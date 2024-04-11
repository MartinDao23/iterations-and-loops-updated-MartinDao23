# Your solution to Exercise 22
b = input("Enter a number")
for x in range (len(b)-1,0,-1):
    for i in range (x): 
        print(b[i], end = "")
    print("")