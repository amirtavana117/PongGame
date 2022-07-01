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
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")

screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")


Game_Is_on = True

while Game_Is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
