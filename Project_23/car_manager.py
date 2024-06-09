from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list:Turtle = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.car_list:
            car.goto(car.xcor()-self.moving_distance, car.ycor())

    def increase_moving_distance(self):
        self.moving_distance += MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.car_list.append(car)
