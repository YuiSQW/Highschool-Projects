import turtle
import time
from snake import snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# fun for making the snake segments

def make_snake(start_posx, start_posy, parts):
    for snake_part in range(parts):
        snake_part = turtle.Turtle("square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(start_posx, start_posy)
        start_posx += -20


make_snake(start_posx=0, start_posy=0, parts=3)
screen.update()

snake_parts = turtle.turtles()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for part_num in range(len(snake_parts) - 1, 0, -1):
        new_x = snake_parts[part_num - 1].xcor()
        new_y = snake_parts[part_num - 1].ycor()
        snake_parts[part_num].goto(new_x, new_y)
    snake_parts[0].forward(20)


screen.exitonclick()
