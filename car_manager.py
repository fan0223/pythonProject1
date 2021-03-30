from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []


class CarManager:
    def __init__(self):
        self.create_car()

    def create_car(self):
        time.sleep(0.5)
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(310, random.randint(-280, 250))
        cars.append(car)

    def car_move(self):
        for car in cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())


