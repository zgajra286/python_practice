# 1)Write a program to print multiplication table of a given number using for loop

num = int(input("Enter a number : "))

for i in range(10,0,-1):  #range(start,end,step_size) as a result easier to print reverse of this table
    print(f"{num} x {i} = {num * i}")

