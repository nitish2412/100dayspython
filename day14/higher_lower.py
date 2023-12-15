from game_data import data
from art import logo, vs
import random

def get_random_account(data):
  return random.choice(data)

def winner(a, b):
  if a > b:
    return "A"
  else:
    return "B"
game_on=True
user_a = get_random_account(data)
score =0
while game_on:
  print(logo)
  print(f"Compare A: {user_a['name']}, a {user_a['description']}, from {user_a['country']}")
  print(vs)
  user_b = get_random_account(data)
  while user_a == user_b:
    user_b = get_random_account(data)
  print(f"Against B: {user_b['name']}, a {user_b['description']}, from {user_b['country']}")
  #print(f"testing A: {user_a['follower_count']}, B: {user_b['follower_count']}")
  user_choice = input("Who has more followers? Type 'A' or 'B':")
  
  if user_choice == winner(user_a['follower_count'],user_b['follower_count']):
    score+=1
    print(f"You are Right, your current score:{score}")
    user_a = user_b
   
  else:
    print(f"Sorry,You Wrong. your total score: {score}")
    game_on = False
    

