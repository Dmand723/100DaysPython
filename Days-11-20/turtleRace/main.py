import random as r
from turtle import Turtle, Screen

class Game():
    def __init__(self):
        self.window = Screen()
        self.window.listen()
        self.colors = ["red","orange","yellow", "green", "blue", "purple"]
        self.yPos = [-70,-40,-10,20,50,80,110]
        self.players = []
        self.playing = False

    def setup(self):
        self.window.setup(width=500,height=400)
        self.userBet = self.window.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        if not self.userBet in self.colors:#if they say a color not in the color list it will add it to the race
                self.colors.append(self.userBet)
            
        for i in range(len(self.colors)):
            turtle = Turtle(shape="turtle")
            turtle.color()
            turtle.penup()
            try:
                turtle.color(self.colors[i])
            except:
                print("That is an invalid color name")
                quit()
            turtle.goto(x=-230,y=self.yPos[i])
            self.players.append(turtle)

    def mainLoop(self):
        while self.playing:
            for t in self.players:
                randDist = r.randint(0,10)
                t.forward(randDist)
                if t.xcor() >= 230 :
                    self.gameEnd(t)
    
    def gameEnd(self,wingingTurtle):
        self.playing = False
        color = wingingTurtle.pencolor()
        if color == self.userBet:
            print('You Win!!')
        else:
            print(f'You Loose! {color} wins')

    def start(self):
        self.playing = True
        self.mainLoop()
        self.window.exitonclick()

def main():
    game = Game()
    game.setup()
    game.start()

if __name__ == "__main__":
    main()




