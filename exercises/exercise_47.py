# Your solution to Exercise 47
n = input("Enter a number")
palindrome = True
for i in range (1,int(n)):
    for x in range (len(str(i))):
        if str(i)[x] != str(i)[(len(str(i))-1)-x]:
            palindrome = False
        else:
            palindrome = True
    if palindrome == True:
        print(i)