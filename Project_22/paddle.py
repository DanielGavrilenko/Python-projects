from turtle import Turtle
HEIGHT = 600

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    def up(self):
        position = self.position()
        if position[1] + 20 + 50 < HEIGHT/2:
            self.goto(position[0], position[1]+20)

    def down(self):
        position = self.position()
        if position[1] - 20 - 50 > -HEIGHT / 2:
            self.goto(position[0], position[1]-20)
