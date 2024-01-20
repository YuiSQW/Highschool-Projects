import turtle
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, start_posx, start_posy, parts):
        self.snake_parts = []
        self.create_snake(start_posx, start_posy, parts)
        self.head = self.snake_parts[0]

    def create_snake(self, start_posx, start_posy, parts):
        """
        Creating a snake input start_posx, start_posy, amount of parts

        """
        for snake_part in range(parts):
            snake_part = turtle.Turtle("square")
            snake_part.penup()
            snake_part.color("white")
            snake_part.speed(0)
            snake_part.goto(start_posx, start_posy)
            start_posx += -20
            self.snake_parts.append(snake_part)

    def add_segment(self):
        snake_part = turtle.Turtle("square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.speed(0)
        snake_part.goto(self.snake_parts[-1].xcor(),
                        self.snake_parts[-1].ycor())
        self.snake_parts.append(snake_part)

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
