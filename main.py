from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle_one = Paddle((350, 0))
paddle_two = Paddle ((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(paddle_one.up, "Up")
screen.onkeypress(paddle_one.down, "Down")
screen.onkeypress(paddle_two.up, "w")
screen.onkeypress(paddle_two.down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    ball.wall_bounce()

    if ball.distance(paddle_one) < 55 and ball.xcor() > 320 or ball.distance(paddle_two) < 55 and ball.xcor() < -320:
        ball.paddle_bounce()
        
            
        
    
    if ball.xcor() > 370:
        
        ball.out_of_bounds()
        scoreboard.increase_score_l()
    
    if ball.xcor() < -370:

         ball.out_of_bounds()
         scoreboard.increase_score_r()

        
        




    

    




















screen.exitonclick()