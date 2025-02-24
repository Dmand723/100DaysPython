from scripts.settings import *

class ScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.score = score
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}",align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        
    def updateScore(self,score):
        self.score = score
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=("Arial", 24, "normal"))

    def gameOver(self):
        self.goto((0,0))
        self.color('white')
        self.write('GAME OVER!\nPress Space To play again',align='center',font=("Arial", 15, "normal"))
        self.hideturtle()