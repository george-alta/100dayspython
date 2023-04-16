from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

REFRESH = 0.1
COLISSION = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(REFRESH)
    snake.move()

    if snake.head.distance(food) < COLISSION:
        food.refresh()

screen.exitonclick()
