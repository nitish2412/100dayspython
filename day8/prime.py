import math
def prime_checker(number):
  n=round(math.sqrt(number))
  flag=0
  for i in range(3,n+1):
    if number%i==0:
      flag=1
  if flag==0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)
