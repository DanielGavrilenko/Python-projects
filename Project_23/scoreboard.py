from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.goto(-220, 240)
        self.print_score()

    def print_score(self):
        self.write(f"Level: {self.lvl}", align="center", font=FONT)

    def increase_lvl(self):
        self.lvl += 1

    def update_score(self):
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
