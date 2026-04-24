# Write a program which finds out whether a given name is present in a list or not.

names = []

while True:
    name = input("Enter names type stop when finished entering names : ").lower()
    if name == "stop":
        break 
    names.append(name)



print("List of names: " , names)   #lists are mutable right

while True :
    search = input(r"Enter name you want to search or type 'stop' to exit : ").lower()

    if search == "stop":
         break
    if search in names :
            print("The name is present in the list")
    
    else :
        print("The name is not present in the list")