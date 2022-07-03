from turtle import Screen
from Ball import Ball
from Paddle import Paddle
import time
from ScoreBoard import Scoreboard
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
score = Scoreboard()
screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")

screen.onkey(l_paddle.Up, "w")
screen.onkey(l_paddle.Down, "s")


Game_Is_on = True

while Game_Is_on:
    screen.update()
    score.update_score_board()
    time.sleep(0.01)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouonce()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.hit()
    if ball.xcor() > 380:
        score.increase_l()
        ball.restart()
    if ball.xcor() < -380:
        score.increase_r()
        ball.restart()


screen.exitonclick()
