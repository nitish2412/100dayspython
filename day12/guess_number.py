#Number Guessing Game Objectives:


import random

def play_game():
  actual_number = random.randint(1,100)
  print("Welcome to guess number game!")
  print("I am thinking number between 1 to 100")
  difficulty = input("Choose a difficulty level. Type 'easy' or 'hard':")
  attempt = 0
  game_on = True
  if difficulty == "easy":
    attempt=10
  elif difficulty == "hard":
    attempt = 5
  else:
    print("please provie a valid difficulty level")
    game_on = False
  
  while game_on:
    print(f"You  have {attempt} attempts remaining to guess the number")
    guess_number = int(input("Make a Guess:"))
    if guess_number == actual_number:
      print(f"You got the number. Actual number is {actual_number}")
      game_on = False
    elif guess_number > actual_number:
      print("To High")
      attempt -=1
    else:
      print("To Low")
      attempt -=1
    if(attempt==0):
      print("You loose the game. please try again")
      game_on =False
game_continue =True
start_flag=1
while game_continue:
  if start_flag == 1:
    play_game()
  start_flag=0
  play_again = input("Do you want to play again. Type 'y' or 'n':").lower()
  if play_again == "y":
    play_game()
  elif play_again == "n":
    game_continue = False
  else:
    print("Please provide a valid input")

