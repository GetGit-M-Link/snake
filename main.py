from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600, startx=2500)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(screen)
while scoreboard.game_is_on:
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="d", fun=snake.right)
    screen.onkey(key="x", fun=scoreboard.game_ends)
    snake.move()
    screen.update()
    time.sleep(0.1)

    # Detects collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.grow()
        scoreboard.add_points()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_ends()

    # Detect collision with snake
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_ends()

screen.exitonclick()
