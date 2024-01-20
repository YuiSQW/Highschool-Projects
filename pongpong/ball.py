from turtle import Turtle, Screen
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, 0)
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1

    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed * 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
