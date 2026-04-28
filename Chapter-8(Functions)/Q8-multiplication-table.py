# 8. Write a python function to print multiplication table of a given number

num=0
n=int(input("Enter the number for which you want to print the table: "))
end = int(input("Enter the range upto which you want the table : "))

def multiplication_table(n,end):
       for i in range(1,end+1):
        
         num=n*i
         print(n,"*",i , "=",num)
       print("Table printed")
        
        
        
multiplication_table(n,end)  