# 1.	Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

word = "twinkle"

with open("./poems.txt","r") as f:
    content = f.read()
    print(content)

    
    words = content.lower().split()

if word in words :
    print("Word found")
else:
    print("Word not found")

