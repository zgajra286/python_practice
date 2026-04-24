# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
# 8. If languages of two friends are same; what will happen to the program in problem
# 6?


dict = {}
name = input('Enter your name =  ')
language = input('Enter your favorite language =  ')
dict.update({name:language})

name = input('Enter your name =  ')
language = input('Enter your favorite language =  ')
dict.update({name:language})

name = input('Enter your name =  ')
language = input('Enter your favorite language =  ')
dict.update({name:language})

name = input('Enter your name =  ')
language = input('Enter your favorite language =  ')
dict.update({name:language})


print(dict)

# Key is the identifier and it cannot be same so when i run update method it gets updated to the most recent input given but values can be same for more then one keys




