# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
text = input("Enter text : ")
print("double space detected AT index : ",text.find("  "))
new_text = text.replace("  "," ")
print(new_text)







