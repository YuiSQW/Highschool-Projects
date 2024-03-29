from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setpos(position)
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def moving_up(self):

        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def moving_down(self):

        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
