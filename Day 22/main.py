from turtle import Screen
from paddles import Paddle
from Ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
paddle_r = Paddle(350)
paddle_l = Paddle(-350)
scoreboard = Scoreboard()
ball = Ball()
screen.setup(height = 600,width = 800)
screen.title("Pong")
screen.bgcolor("black")
screen.listen()
screen.onkey(fun = paddle_r.up,key = "i")
screen.onkey(fun = paddle_r.down,key = "k")
screen.onkey(fun = paddle_l.up,key = "w")
screen.onkey(fun = paddle_l.down,key = "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall()
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50:
        ball.reflect()
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.reflect()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()
screen.exitonclick()
