from telnetlib import FORWARD_X
from turtle import Turtle, up
FORWARD = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(350, 0)

    def Up(self):
        new_y = self.ycor() + FORWARD
        self.goto(self.xcor(), new_y)
