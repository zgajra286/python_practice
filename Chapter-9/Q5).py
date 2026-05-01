# 5.	Repeat program 4 for a list of such words to be censored. 
words = ["donkey","bad","dumb"]


with open("censor.txt","r") as f:
        content = f.read()
        print(content)

for word in words:
        content = content.replace(word, "#"*len(word))
print(content)

with open("censor.txt" , "w") as f:
        f.write(content)