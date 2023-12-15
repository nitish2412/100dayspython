from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#we can select question from: https://opentdb.com/api_config.php
question_bank = []
for q in question_data:
    new_q = Question(q['text'], q['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!!!!!")
print(f"your final score :{quiz.score}/{quiz.question_number}")
