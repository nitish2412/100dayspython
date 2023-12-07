#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#n=len(word_list)
#rand_int=random.randint(0,n-1)
#word=word_list[rand_int]

word=random.choice(word_list)

guess_letter=input("Guess a letter: ")

for l in word:
  if l==guess_letter:
    print("Right")
  else:
    print("Wrong")

print("Correct word is:",word)
