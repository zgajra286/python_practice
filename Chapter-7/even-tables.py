# Print only the tables of 2, 4, and 6, from 1 to 5.
for even in range(2,7,2):
  print("Table for : " , even)
  for num in range(1,6):
      answer = even * num
      print(even ,"*" , num,"=",answer)