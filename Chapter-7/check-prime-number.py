n = int(input("Check whether the number is prime or not: "))
for i in range(2,n):
  if(n % i) == 0:
   print("not a prime number")
   break

else:
    print("Entered number is a prime number")
    