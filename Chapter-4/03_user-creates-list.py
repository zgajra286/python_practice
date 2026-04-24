# 1)Write a program to store seven fruits in a list entered by the user.

fruits = []

for i in range(7):
    name = input(f"Enter fruit {i+1}: ")
    fruits.append(name)

print("Fruit list:", fruits)

# 2)Write a program to accept marks of 6 students and display them in a sorted
# manner.

# marks = []
# for i in range(6):
#     student = input(f"Marks for roll-no {i+1}: ")
#     marks.append(student)
    
# print(marks)