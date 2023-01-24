import turtle
from turtle import Turtle, Screen
import random
from paddle_1 import Paddle
from ball import Ball
import time
from score import Score


PADDLE_SPEED = 0.001
BALL_DIRECTION = random.randint(-80, 80)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)



player_1 = Paddle((-350, 0))

player_2 = Paddle((350, 0))

bola = Ball()

score_1 = Score()
score_1.writer(x=120, y=240)

score_2 = Score()
score_2.writer(x=-150, y=240)

score_divider = Score()
score_divider.divider()



# score_2 = Score()
# score_2.score(-100, 400)

screen.listen()

screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")



bola.setheading(BALL_DIRECTION)

game = True
while game:
    time.sleep(bola.move_speed)
    screen.update()
    bola.move()

    # print(bola.ycor())
    if bola.ycor() > float(280) or bola.ycor() < float(-280):
        bola.bouce()

    if bola.distance(player_1) < 50 and bola.xcor() < -320:
        bola.retort()


    if bola.distance(player_2) < 50 and bola.xcor() > 320:
        bola.retort()


    if bola.xcor() > 380:
        score_1.clear()
        score_1.points += 1
        score_1.writer(x=120, y=240)
        bola.restart()


    if bola.xcor() < -380:
        score_2.clear()
        score_2.points += 1
        score_2.writer(x=-150, y=240)
        bola.restart()

    #
    # if bola.distance(player_1.posi())  < 35:
    #     x = 270 + bola.heading()
    #     bola.setheading(x)
    #     BALL_DIRECTION = float(x)
    # elif bola.distance(player_2.posi()) < 35 :
    #     x = 270 + bola.heading()
    #     bola.setheading(x)
    #     BALL_DIRECTION = float(x)
    # elif bola.ycor() > float(290) or bola.ycor() < float(-290):
    #     x = 360 - BALL_DIRECTION
    #     bola.setheading(x)
    #     BALL_DIRECTION = float(x)
    # elif bola.xcor() < float(-400):
    #     score_2.scoreer()
    #     score_2.clear()
    #     score_2.points += 1
    #     score_2.writer(x=150, y=240)
    #     bola.restart()
    #     bola.setheading(random.randint(-80, 80))
    # elif bola.xcor() > float(400):
    #     score_1.scoreer()
    #     score_1.clear()
    #     score_1.points += 1
    #     score_1.writer(x=-150, y=240)
    #     bola.restart()
    #     bola.setheading(random.randint(100, 370))
    # bola.fd(20)


































screen.exitonclick()