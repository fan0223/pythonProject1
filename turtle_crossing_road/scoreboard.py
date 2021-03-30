from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)

    def level_update(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
