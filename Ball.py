from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed("fastest")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bouonce(self):
        self.y_move *= -1

    def hit(self):
        self.y_move *= -1
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
