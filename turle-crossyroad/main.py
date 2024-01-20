import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
speed = 0.1

player = Player()
scoreboard = Scoreboard()

all_cars = []
screen.onkey(fun=player.movement, key="Up")


game_is_on = True
count = 5
while game_is_on:
    scoreboard.update_level()

    time.sleep(speed)
    screen.update()
    count += 1

    if count % 6 == 0:
        car = CarManager()
        all_cars.append(car)

    for car in all_cars:

        car.movement()
        if car.distance(player) < 20:

            game_is_on = False

    if player.ycor() >= 270:
        player.reset_pos()
        scoreboard.level += 1
        speed = speed * 1.1


screen.exitonclick()
