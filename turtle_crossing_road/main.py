import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")
scoreboard = Scoreboard()

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    if count % 6 == 0:
        car_manager.create_car()
    count += 1

    if player.ycor() > player.end_line:
        player.next_level()
        scoreboard.level_update()
        car_manager.car_update()
        print(car_manager.car_move_distance)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
