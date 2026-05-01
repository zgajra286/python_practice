
# 4.	A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.  
with open("content_donkey.txt","r") as f:
    content = f.read().lower().split()

    # print(type(content))

content = ["#####" if w =="donkey" else w for w in content]
with open("content_donkey.txt","w") as f:
    f.write("  ".join(content))
 
    
    
    
    
