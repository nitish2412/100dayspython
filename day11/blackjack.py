import random
from art import logo


def deal(cards):
    return random.choice(cards)


def game_start(cards):
    user_cards = []
    computer_cards = []
    i = 0
    while i < 2:
        user_cards.append(deal(cards))
        computer_cards.append(deal(cards))
        i += 1
    return user_cards, computer_cards


def calculate_score(cards):
    score = sum(cards)
    if score == 21:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score
def print_hand(user_cards,computer_cards):
  print(f"Your Cards: {user_cards} Your score: {calculate_score(user_cards)}")
  print(f"Computer First Card: {computer_cards} computer score: {calculate_score(computer_cards)}")


def play_game():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards, computer_cards = game_start(cards)
  
  print(f"Your Cards: {user_cards} Your score: {calculate_score(user_cards)}")
  print("Computer First Card: ", computer_cards[0])
  
  game_on = True
  while game_on:
      choice = input("Do you want to draw another card? type 'y' or 'n' ")
      if choice == "y":
          user_cards.append(deal(cards))
          print(f"Your Cards: {user_cards} Your score: {calculate_score(user_cards)}")
          print("Computer First Card: ", computer_cards[0])
          user_score = calculate_score(user_cards)
          if user_score == 0:
              print_hand(user_cards, computer_cards)
              print("You win, with a blackjack!")
              game_on = False
          elif (user_score > 21):
              print_hand(user_cards, computer_cards)
              print("You loose")
              game_on = False
      elif choice == "n":
          computer_score = calculate_score(computer_cards)
          user_score = calculate_score(user_cards)
          if computer_score == 0:
              print_hand(user_cards, computer_cards)
              print("You loose, opponenent has a blackjack!")
              game_on = False
  
          if (user_score < 17):
              print("You loose")
              game_on = False
          else:
              while computer_score < 17:
                  computer_cards.append(deal(cards))
                  computer_score = calculate_score(computer_cards)
              print_hand(user_cards, computer_cards)
              if (computer_score == user_score):
                  print("Draw!!!!!")
                  game_on = False
              elif (user_score > 21):
                  print("You loose")
                  game_on = False
              elif (computer_score > 21):
                  print("You win")
                  game_on = False
              elif (computer_score > user_score):
                  print("You loose")
                  game_on = False
              else:
                  print("you win")
                  game_on = False
      else:
          print("Please provide a correct input")
while(input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=="y"):
  play_game()
