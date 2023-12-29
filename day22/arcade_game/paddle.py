from turtle import Turtle


class Paddle:
    def __init__(self, position):
        self.initial_pos = position
        self.paddle = self.create_paddle()

    def goto_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def goto_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def create_paddle(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(self.initial_pos)
        return paddle
