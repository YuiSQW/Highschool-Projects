from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.setpos(-200, 250)
        self.level = 1

    def update_level(self):
        self.clear()
        self.write((f"Level: {self.level}"), align="center", font=FONT)
