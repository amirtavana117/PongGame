from turtle import Screen
from Paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()
screen.listen()

screen.onkey(paddle.Up, "Up")


screen.exitonclick()
