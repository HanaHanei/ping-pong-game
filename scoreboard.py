from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()


    def update(self):
        self.clear()
        self.goto(200, 270)
        self.write(f"Score:{self.r_score}", align="center", font=("Cooper Black", 18, "italic"))
        self.goto(-200, 270)
        self.write(f"Score:{self.l_score}", align="center", font=("Cooper Black", 18, "italic"))

    def Left_score(self):
        self.l_score+=1
        self.update()

    def Right_score(self):
        self.r_score+=1
        self.update()