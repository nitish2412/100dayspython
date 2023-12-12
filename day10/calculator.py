from art import logo
#add
def add(n1,n2):
  return n1+n2

#subtract
def subtract(n1, n2):
  return n1-n2

#multiply
def multiply(n1,n2):
  return n1*n2

#divide
def divide(n1, n2):
  return n1/n2
operations ={
  "+" :add,
  "-" :subtract,
  "*" :multiply,
  "/" :divide 
}

def calculator():
  print(logo)
  num1 = float(input("what is the first number? "))
  
  
  for key in operations:
    print(key)
  should_continue =True
  while should_continue:
    operation_symbol= input("pick an operation : ")
    if operation_symbol not in operations.keys():
      print("Please provide a valid symbol")
      continue
    num2 = float(input("what is the next number? "))
    calculation=operations[operation_symbol]
    answer=calculation(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculatiing with {answer}, or type 'n' to start with new calculation, type anything else to exit calculation :")
    if(choice =="y"):
      num1=answer
    elif choice =="n":
      should_continue= False
      calculator()
    else:
      should_continue=False

calculator()




