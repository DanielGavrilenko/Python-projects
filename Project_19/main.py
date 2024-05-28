from turtle import Turtle, Screen
import random

TURTLE_NUMBER = 6
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter color:")
turtles = []
winner = -1


def go_forward(my_turtle: Turtle):
    step = random.randint(10, 30)
    my_turtle.forward(step)


def creating_turtles():
    for i in range(TURTLE_NUMBER):
        current_turtle = Turtle(shape="turtle")
        current_turtle.penup()
        if i == 0:
            current_turtle.color("green")
            current_turtle.goto(x=-230, y=-100)
            turtles.append(current_turtle)
        if i == 1:
            current_turtle.color("blue")
            current_turtle.goto(x=-230, y=-60)
            turtles.append(current_turtle)
        if i == 2:
            current_turtle.color("yellow")
            current_turtle.goto(x=-230, y=-20)
            turtles.append(current_turtle)
        if i == 3:
            current_turtle.color("purple")
            current_turtle.goto(x=-230, y=20)
            turtles.append(current_turtle)
        if i == 4:
            current_turtle.color("red")
            current_turtle.goto(x=-230, y=60)
            turtles.append(current_turtle)
        if i == 5:
            current_turtle.color("black")
            current_turtle.goto(x=-230, y=100)
            turtles.append(current_turtle)


creating_turtles()
while winner == -1:
    for i in range(TURTLE_NUMBER):
        go_forward(turtles[i])
        if turtles[i].xcor() >= 210:
            winner = i
print(f"{turtles[winner].pencolor()} finished the ace first")
if turtles[winner].pencolor() == user_bet:
    print("You guessed the winner")
else:
    print("You didn't guess the winner")
screen.exitonclick()
