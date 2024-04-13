# Your solution to Exercise 51
a = input("Enter a number")
b= input("Enter a number")
for i in range (int(a),int(b)):
    if str(i)[0] == str(i)[1] == str(i)[2]:
        identical = True
    elif str(i)[0] == str(i)[2] == str(i)[3]:
        identical = True
    elif str(i)[0] == str(i)[1] == str(i)[3]:
        identical = True
    elif str(i)[1] == str(i)[2] == str(i)[3]:
        identical = True
    else:
        identical = False
    if identical == True:
        print(i)