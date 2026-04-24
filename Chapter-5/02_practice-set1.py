# 1) Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!



words = {
    "madad" : "help",
    "khursi" : "chair",
    "billi" : "cat"
}
word =  input("Enter the Hindi word which you want the meaning for : ")
key = word.lower()
print(words[key])
