from turtle import Screen
from Ball import Ball
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
ball = Ball()

screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")

screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")


Game_Is_on = True

while Game_Is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouonce()


screen.exitonclick()
