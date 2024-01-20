import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PLayin bong")
screen.tracer(0)
game_is_on = True


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(fun=r_paddle.moving_up, key="Up")
screen.onkey(fun=r_paddle.moving_down, key="Down")

screen.onkey(fun=l_paddle.moving_up, key="w")
screen.onkey(fun=l_paddle.moving_down, key="s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.ycor() >= 280 or ball.ycor() <= - 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
