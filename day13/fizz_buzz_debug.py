target = int(input())
for number in range(1, target + 1):
  #if number % 3 == 0 or number % 5 == 0: #buggy code
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  #if number % 3 == 0: #buggy code
  elif number % 3 == 0:
    print("Fizz")
  #if number % 5 == 0: #buggy code
  elif number % 5 == 0:
    print("Buzz")
  else:
    #print([number])
    print(number) #buggy code
