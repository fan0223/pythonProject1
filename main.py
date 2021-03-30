import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager = CarManager()
    car_manager.car_move()

    if player.ycor() > 270:
        player.next_level()
        scoreboard.level_update()

    if player.distance(car_manager) < 20:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()
