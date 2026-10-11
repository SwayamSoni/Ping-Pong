from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.teleport(x,0)
        self.shapesize(stretch_wid= 5,stretch_len = 1 )
    def up(self):
        self.teleport(self.xcor(),self.ycor() + 20)
    def down(self):
        self.teleport(self.xcor(),self.ycor() - 20)



