'''
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100
rows = 10
cols = 10
forward_step = 50
dot_size = 20
for _ in range(rows):

    for _ in range(cols):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(forward_step)

    tim.setheading(90)
    tim.forward(forward_step)
    tim.setheading(180)
    tim.forward(forward_step*cols)
    tim.setheading(0)


'''
for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
'''
screen = turtle_module.Screen()
screen.exitonclick()
