# 1) Remove extra spaces and convert to lowercase
# 2) Count number of words
# text = input("Enter text :")
# clean = text.strip().lower()
# print(clean)
# print("Count number of words: " ,  len(clean))

import string

s = input().lower()

for p in string.punctuation:
    print(p)
    s = s.replace(p, "")

words = s.split()
print(words)

print(len(words))
