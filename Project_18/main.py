import turtle
from turtle import Turtle, Screen
import colorgram
import random


my_turtle = Turtle()
screen = Screen()

'''
my_turtle.shape("turtle")
for i in range(3, 6):
    for y in range(i):
        my_turtle.forward(50)
        my_turtle.left(360/i)
'''


def extracting_colors():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb_colors.append(color.rgb)
    return rgb_colors


def drawing_points(colors):
    for i in range(10):
        for y in range(10):
            current_color = random.choice(colors)
            my_turtle.dot(20, (current_color[0], current_color[1], current_color[2]))
            position = my_turtle.position()
            my_turtle.teleport(position[0] + 50, position[1])
        position = my_turtle.position()
        my_turtle.teleport(position[0] - 50 * 10, position[1] + 50)


colors = extracting_colors()
turtle.colormode(255)
my_turtle.teleport(-200,-200)
drawing_points(colors)
screen.exitonclick()