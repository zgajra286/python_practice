# 3.	Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old. 

n=1
def tables():
    for n in range(2,21):
        with open(f"tables/table_of_{n}.txt" , "w") as f:
             
         for i in range(1,11):
               result = n*i 
               f.write(f"{n}*{i}={result}\n")
            
        print()
tables()

