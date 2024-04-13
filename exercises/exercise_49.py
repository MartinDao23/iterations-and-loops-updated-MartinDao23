# Your solution to Exercise 49
a = input("Enter a number")
b = input("Enter a number")
palindrome = True
for i in range (int(a),int(b)):
    palindrome = True
    for x in range (len(str(i))):
        if str(i)[x] != str(i)[(len(str(i))-1)-x]:
            palindrome = False
    if palindrome == True:
        print(i)