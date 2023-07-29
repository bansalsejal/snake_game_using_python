from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.create()

    def create(self):
        x = random.randint(-300, 300)
        y = random.randint(-310, 310)
        self.setposition(x, y)
