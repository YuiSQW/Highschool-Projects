from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.score = 0
        self.penup()
        self.setpos(0, 260)
        self.get_score()

    def get_score(self):
        self.write(("Score: {}").format(self.score), align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.get_score()
