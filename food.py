from turtle import Turtle, Screen
import random


class FOOD(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.new_position()

    def new_position(self):
        self.goto(x=random.randint(-300, 300), y=random.randint(-260, 260))
