import random
import traceback
import turtle
from turtle import Turtle, Screen

tim = Turtle()

#timmy_the_turtle.shape("turtle")
#tim.color("red")

#Draw a square
'''
for _ in range(4):
    t.forward(100)
    t.right(90)
'''
'''
#draw a dotted line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''
'''
#draw triangle, square, pentagon,......
color_list = ['red', 'green', 'blue', 'yellow', 'violet', 'magenta', 'brown', 'black']
color_ind = 0
def draw_shapes(num_side):
    degree = int(360 / num_side)
    tim.color(random.choice(color_list))
    for j in range(num_side):
        tim.forward(100)
        tim.right(degree)
for shape_sides in range(3, 10):
    draw_shapes(shape_sides)
'''


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# draw a random walk
'''
turtle.colormode(255)
color_list = ['red', 'green', 'blue', 'yellow', 'violet', 'magenta', 'brown', 'black']
direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    #tim.color(random.choice(color_list))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
'''


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)


turtle.colormode(255)
#tim.pensize(5)
tim.speed("fastest")
draw_spirograph(2)



screen = Screen()
screen.exitonclick()