# food.py
from turtle import Turtle
import random


class Food(Turtle):  # by using inheritance, you don't need to create a Turtle object now to use the methods and
    # attributes.

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # default is 20 * 20 pixels, but we want 10 * 10
        self.color("blue")
        self.speed("fastest")

        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)