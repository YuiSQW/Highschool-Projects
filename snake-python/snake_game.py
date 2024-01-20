import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


# fun for making the snake segments

def make_snake(start_posx, start_posy, parts):
    for snake_part in range(parts):
        snake_part = turtle.Turtle("square")
        snake_part.color("white")
        snake_part.setpos(start_posx, start_posy)
        start_posx += -20


make_snake(start_posx=0, start_posy=0, parts=3)

snake_parts = turtle.turtles()


screen.exitonclick()
