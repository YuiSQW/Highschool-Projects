import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(298, random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.x_pos = 296
        self.speed = MOVE_INCREMENT

    def movement(self):
        self.x_pos = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(self.x_pos, self.ycor())
