from turtle import Turtle, Screen
import random

my_turtle = Turtle(shape="turtle")
screen = Screen()


def go_ahead():
    my_turtle.forward(10)


def go_back():
    my_turtle.backward(10)


def go_left():
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)


def go_right():
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)


def clear_all():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()
screen.onkey(fun=go_ahead, key="w")
screen.onkey(fun=go_back, key="s")
screen.onkey(fun=go_right, key="a")
screen.onkey(fun=go_left, key="d")
screen.onkey(fun=clear_all, key="c")
screen.exitonclick()

