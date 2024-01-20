from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.y_move = 0

    def reset_pos(self):
        self.setpos(STARTING_POSITION)

    def movement(self):
        self.y_move = self.ycor() + MOVE_DISTANCE
        self.goto(0, self.y_move)
