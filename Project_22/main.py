from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
RIGHT_PADDLE = 350
LEFT_PADDLE = -350

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()

right_paddle = Paddle(RIGHT_PADDLE)
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

left_paddle = Paddle(LEFT_PADDLE)
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # detect collision with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_paddle()
    # detect collision with paddle
    if ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_paddle()
    # detect missing ball on left side
    if ball.xcor() < -350:
        ball.center_ball()
        scoreboard.right_point()
    # detect missing ball on right side
    if ball.xcor() > 350:
        ball.center_ball()
        scoreboard.left_point()




screen.exitonclick()