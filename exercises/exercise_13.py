# Your solution to Exercise 13
password = input("Actual password: ")
attempt = input("What  is the password: ")
while attempt != password:
    print("error")
    attempt = input("What  is the password: ")
print("Done")