import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()
scorebard=Scoreboard()

screen.onkey(l_paddle.W_up, "w")
screen.onkey(l_paddle.S_down, "s")
screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.Down, "Down")
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.Move_upper_right()
    if ball.ycor() > 280 or  ball.ycor() < -280:
        ball.y_bouncing()

    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.x_bouncing()

    if ball.xcor()>380:
        ball.Reset_r()
        scorebard.Left_score()
    if ball.xcor()<-380:
        ball.Reset_r()
        scorebard.Right_score()



screen.exitonclick()
