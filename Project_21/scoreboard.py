from turtle import Turtle
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()

    def write_score(self, score: int):
        self.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    def refresh_score(self, score: int):
        self.clear()
        self.write_score(score)

    def game_over(self):
        self.clear()
        self.goto(0 , 0)
        self.write(arg=f"Game is over", move=False, align="center", font=FONT)

