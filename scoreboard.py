from turtle import Turtle

FONT = (
    "Courier",
    24,
    "normal"
)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)