from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My snake game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.write_score()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Collision with food
    if snake.segments[0].distance(food) < 10:
        snake.extend()
        scoreboard.increase_score()
        food.refresh_food()
        scoreboard.refresh_score()
    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.update_high_score()
        snake.reset()
    # Collision with tail
    if snake.check_tail_collision():
        scoreboard.update_high_score()
        snake.reset()


screen.exitonclick()
