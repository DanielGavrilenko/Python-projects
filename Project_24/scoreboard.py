from turtle import Turtle
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.read_score()

    def read_score(self):
        with open("data.txt", "r") as read_file:
            self.high_score = int(read_file.read())

    def write_score_in_file(self):
        with open("data.txt", mode="w") as write_file:
            write_file.write(f"{self.high_score}")


    def write_score(self):
        self.write(arg=f"Score: {self.score}, High Score:{self.high_score}", move=False, align="center", font=FONT)

    def refresh_score(self):
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0 , 0)
        self.write(arg=f"Game is over", move=False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score_in_file()
        self.refresh_score()
