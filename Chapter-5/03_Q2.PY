# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

numbers = set()
for i in range(8):
    num = int(input(f"Enter the number {i+1}: "))
    numbers.add(num)

   
print(numbers)

# What changed
#1) Python uses indentation to define scope.
# 2)Anything aligned with for is outside the loop.
# 3)Now the set prints only once, showing all unique val