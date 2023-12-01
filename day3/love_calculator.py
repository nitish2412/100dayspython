print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is your partner name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name=name1+name2
name=name.lower()
#calculate true score
true_score=0
true_score+=name.count('t')
true_score+=name.count('r')
true_score+=name.count('u')
true_score+=name.count('e')
#calculate love score
love_score=0
love_score+=name.count('l')
love_score+=name.count('o')
love_score+=name.count('v')
love_score+=name.count('e')

final_score=int(str(true_score)+str(love_score))

if final_score<10 or final_score >90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")



