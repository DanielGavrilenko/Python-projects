from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.number_segments = 3
        for i in range(self.number_segments):
            my_turtle = Turtle(shape="square")
            my_turtle.color("black")
            my_turtle.penup()
            my_turtle.goto(STARTING_POSITION[i])
            self.segments.append(my_turtle)
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(self.number_segments - 1, 0, -1):
            new_position_x = self.segments[seg_num - 1].xcor()
            new_position_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_position_x, new_position_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
