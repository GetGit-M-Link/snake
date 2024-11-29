from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.hideturtle()  # teleport
        self.setposition(x=random_x, y=random_y)
        self.showturtle()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.setposition(x=random_x, y=random_y)




