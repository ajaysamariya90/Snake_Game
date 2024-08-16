from turtle import Turtle
import random

# Here Turtle class is inherit into Food class


class Food(Turtle):

    """So, here we don't need to create an object to call Turtle class we can directly use all the method from Turtle
    class like shown below"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("Red")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)


'we can write like this also but we can inherit the Turtle class into Food class'
# self.timmy = Turtle()
# self.timmy.shape("circle")
