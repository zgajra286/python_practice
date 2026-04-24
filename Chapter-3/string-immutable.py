
# why are strings called immutable when i am able to change the text like this 
# the answer is you had to create a new variable and store a new string you replaced the word but then had to store the string in a new variable 
text = "My name is harry"
print(text.split())  #original string
print(text.strip().lower())   #.strip() removes unwanted characters from the beginning and end of a string (not from the middle).
immutable = text.replace("name" , "not name")
print(immutable)  #duplicate copy 


# immutable
name = "Zeel Gajra"
name[0].replace("Z" , "N") 
print(name)