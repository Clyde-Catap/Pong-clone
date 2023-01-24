from turtle import Turtle

divider_location = [(0, -280), (0, -240), (0, -200), (0, -160), (0, -120), (0, -80), (0, -40), (0, 0), (0, 40), (0, 80), (0, 120), (0, 160), (0, 200),
                    (0, 240), (0, 280)]



class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.points = 0

    def writer(self, x, y):
        self.setposition(x, y)
        self.write(arg=f"{self.points}", move=False, font=("Arial", 45, "bold"))

    def divider(self):
        for x in divider_location[:7]:
            tortle = Turtle()
            tortle.shape("square")
            tortle.showturtle()
            tortle.color("white")
            tortle.penup()
            tortle.shapesize(stretch_wid=1, stretch_len=0.5)
            tortle.goto(x)
        for x in divider_location[8:]:
            tortle = Turtle()
            tortle.shape("square")
            tortle.showturtle()
            tortle.color("white")
            tortle.penup()
            tortle.shapesize(stretch_wid=1, stretch_len=0.5)
            tortle.goto(x)
        for x in divider_location[7:8]:
            tortle = Turtle()
            tortle.shape("square")
            tortle.showturtle()
            tortle.color("white")
            tortle.penup()
            tortle.shapesize(stretch_wid=1, stretch_len=1)
            tortle.goto(x)



