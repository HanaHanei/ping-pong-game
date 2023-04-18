from turtle import Turtle
import random

#create ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed=0.1

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def Move_upper_right(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move

        self.goto(x, y)
        print(x, y)

    def y_bouncing(self):
        self.y_move *= -1


    def x_bouncing(self):
        self.x_move *= -1
        self.ball_speed*=0.9


    def Reset_r(self):
       self.goto(0,0)
       self.ball_speed= 0.1
       self.x_bouncing()