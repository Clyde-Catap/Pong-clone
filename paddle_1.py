from turtle import Turtle

STARTING_LOCATION = (-350, 0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

SPEED = "fastest"


class Paddle(Turtle):


    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(DOWN)
        self.penup()
        self.goto(x)



    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        # return print(self.paddle.ycor())


    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        # return print(self.paddle.ycor())










