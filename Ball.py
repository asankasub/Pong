from turtle import Turtle

class Ball(Turtle):

    def __init__(self):

        super().__init__()
        
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
       
       
     
        

    def ball_move(self):

        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_bounce(self):


        if self.ycor() > 280 or self.ycor() < -280:

           self.ymove *= -1
    
    def paddle_bounce(self):

        self.xmove *= -1
        self.move_speed *= 0.9
        
        
    def out_of_bounds(self):

            self.goto(0,0)
            self.xmove *= -1
            self.move_speed = 0.1
    


    
            

            


        
        
          
   
    
        


        




        
            