from turtle import Turtle

Down = 270
Up = 90


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(self.position)

    def Up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def W_up(self):
        new_y=self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def S_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


