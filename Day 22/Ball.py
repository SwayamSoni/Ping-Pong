from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.move_speed = 0.1
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid= 1, stretch_len = 1)
        self.x = 0
        self.y = 0
        self.change_x = 10
        self.change_y = 10

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        self.teleport(self.x, self.y)

    def wall(self):
        self.change_y *= -1

    def reflect(self):
        self.change_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.x = 0
        self.y = 0
        self.teleport(self.x,self.y)
        self.change_x *= -1
        self.move_speed = 0.1




