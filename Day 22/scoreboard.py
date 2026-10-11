from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.teleport(-100,200)
        self.write(self.l_score,align = 'center',font = ("Arial",80,'normal'))
        self.teleport(100, 200)
        self.write(self.r_score, align='center', font=("Arial", 80, 'normal'))

    def update_score(self):
        self.clear()
        self.teleport(-100, 200)
        self.write(self.l_score, align='center', font=("Arial", 80, 'normal'))
        self.teleport(100, 200)
        self.write(self.r_score, align='center', font=("Arial", 80, 'normal'))


