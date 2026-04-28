# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

def remove_word(lst, word):
    word = word.strip().lower()

    for item in lst:
        if item.lower() == word:
            lst.remove(item)
            break

    return lst
names = ["Tom", "Dick", "Harry"]
print(names)

remove_name = input("Enter name to remove: ")

print(remove_word(names, remove_name))
