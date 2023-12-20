import random
import turtle
from turtle import Turtle, Screen


def create_turtle():
    turtles = []
    y_cor = 80
    for i in range(6):
        tim = Turtle(shape="turtle")
        tim.color(color_list[i])
        tim.penup()
        tim.goto(x=-230, y=y_cor)
        y_cor -= 40
        turtles.append(tim)
    return turtles


screen = Screen()
screen_width = 500
scree_height = 400
screen.setup(width=screen_width, height=scree_height)
screen.title("Racing Game")
is_race_on = False
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = create_turtle()

user_bet = screen.textinput(title="Make your bet.", prompt="which turtle win the race? choose a color")
print(user_bet)
if user_bet:
    is_race_on = True
winning_color = ""
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            break
        randon_dist = random.randint(1, 5)
        turtle.forward(randon_dist)
if user_bet == winning_color:
    print(f"You've won the race. The {winning_color} turtle is winner!")
else:
    print(f"You've loss the race. The {winning_color} turtle is winner!")


screen.exitonclick()