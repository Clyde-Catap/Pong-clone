import turtle
from turtle import Turtle, Screen
import random
from paddle_1 import Paddle

from ball import Ball
import time


PADDLE_SPEED = 0
screen = Screen()
screen.setup(width=1500, height=900)
screen.bgcolor("black")
# screen.tracer(0)


tortle = Turtle()
divider_location = [(0, -40), (0, -80), (0, -120), (0, -160), (0, 0), (0, 40), (0, 80), (0, 120), (0, 160)]

for x in divider_location[:4]:
    tortle = Turtle()
    tortle.shape("square")
    tortle.showturtle()
    tortle.color("white")
    tortle.penup()
    tortle.shapesize(stretch_wid=1, stretch_len=0.5)
    tortle.goto(x)
for x in divider_location[5:]:
    tortle = Turtle()
    tortle.shape("square")
    tortle.showturtle()
    tortle.color("white")
    tortle.penup()
    tortle.shapesize(stretch_wid=1, stretch_len=0.5)
    tortle.goto(x)
for x in divider_location[4:5]:
    tortle = Turtle()
    tortle.shape("square")
    tortle.showturtle()
    tortle.color("white")
    tortle.penup()
    tortle.shapesize(stretch_wid=1, stretch_len=1)
    tortle.goto(x)

    # bola.move()

screen.exitonclick()