from turtle import Turtle
FORWARD = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def Up(self):
        new_y = self.ycor() + FORWARD
        self.goto(self.xcor(), new_y)

    def Down(self):
        new_y = self.ycor() - FORWARD
        self.goto(self.xcor(), new_y)
