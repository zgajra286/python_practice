# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

name = input("Enter name : ")
print(name,"Good Afternoon")

# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

import datetime
x = datetime.datetime.now().date()


letter = f'''Dear {name},
      You are selected!
      {x}'''
      
print(letter)



