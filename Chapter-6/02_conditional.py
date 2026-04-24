# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user


mks1 = int(input("Enter your Science marks: "))
mks2 = int(input("Enter your Maths marks: "))
mks3 = int(input("Enter your English marks: "))
total = (mks1+mks2+mks3)/3

print((total))

if total >=40:
    print(r"Total is above 40% ")

if mks1>=33 and mks2>=33 and mks3 >=33:
    print("Student passed in indivisual subjects")
elif mks1<33 and mks2<33 and mks3<33:
    print("Student has failed in All Subjects")
elif mks1<33 and mks2<33 and mks3>33:
    print("Student failed in Science and Maths")
elif mks3<33 and mks1<33 and mks2>33:
    print("Student failed in Science and  English") 
elif mks3<33 and mks1>33 and mks2<33:
    print("Student failed in Maths and  English")  
else :
    print("Student failed in all subjects")