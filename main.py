from turtle import Screen
from Paddle import Paddle
import time
# Initial SCcreen
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
paddle = Paddle()

screen.onkey(paddle.Up, "Up")
screen.onkey(paddle.Down, "Down")


Game_Is_on = True

while Game_Is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
