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
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(self.number_segments):
            self.add_segment(STARTING_POSITION[i])

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position_x = self.segments[seg_num - 1].xcor()
            new_position_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_position_x, new_position_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        my_turtle = Turtle(shape="square")
        my_turtle.color("black")
        my_turtle.penup()
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def check_tail_collision(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False

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

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
