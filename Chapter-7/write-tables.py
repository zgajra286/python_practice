num = int(input("Enter a number : "))
end = int(input("Enter the range upto which you want the table : "))
count= 1
while count<=end:
  total = num * count
  print(num ,"*" ,count ,"=" ,total)
  count = count +1