from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(310, random.randint(-280, 250))
        self.car_move()

    def car_move(self):
        new_x = self.xcor()-MOVE_INCREMENT
        self.goto(new_x, self.ycor())


