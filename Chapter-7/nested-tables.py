# Create full tables from 1 to 10 for numbers 1 to 10 (nested loops).


for num in range(1,10):
  print("Table of: " , num)

  for table in range(1,10):
    
       answer = table * num  
       print(num , "*",table ,"=", answer)

print()

   