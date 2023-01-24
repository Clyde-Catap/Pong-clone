from turtle import Turtle
import random

 # 60

SPEED = "slowest"

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        # self.bola = Turtle()
        # self.angle = random.randint(-40, 40)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

        # self.direction = random.choice(BALL_DIRECTION)

    def restart(self):
        self.setposition(0, 0)
        self.retort()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bouce(self):
        self.y_move *= -1


    def retort(self):
        self.x_move *= -1
        self.move_speed *= 0.6






    # def move(self):
    #     if self.direction == "left":
    #         d = random.randint(149, 212)
    #         self.bola.setheading(d)
    #         while self.bola.xcor() != -750:
    #             self.bola.forward(20)
    #
    #
    #     elif self.direction == "right":
    #         d = random.randint(-31, 32)
    #         self.bola.setheading(d)
    #         while self.bola.xcor() != 750:
    #             self.bola.forward(20)






    # def bouncer(self, d):
    #     self.bola.setheading(d+180)




