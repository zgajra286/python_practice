# Write a program to find whether a given username contains less than 10
# characters or not.

username = input("Enter your username: ")
check = len(username)
print(check)
if check<=10 :
    print ("Valid username")
else:
    print("Invalid username"    )