from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.backward(self.car_move_distance)

    def car_update(self):
        self.car_move_distance += MOVE_INCREMENT
