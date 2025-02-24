from scripts.settings import *

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        
        self.move()
    
    def move(self):
        pos = (r.randint(-280,280),r.randint(-280,280))
        self.goto(pos)