from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# screen set
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.rescore()
    # 蛇與牆壁碰撞
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    # 蛇與尾巴碰撞
    for sna in snake.snakes[1:]:
        if snake.head.distance(sna) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
