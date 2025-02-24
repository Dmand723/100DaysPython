from turtle import Turtle, Screen
import random as r 
import colorgram  
class Paint():
    def __init__(self):
        self.draw = Turtle()
        self.window = Screen()
        self.window.title("Awsome Paiting")
        self.rgbColours =[]
        self.curPosX = 400
        
        self.curPosY = -350
        self.move()
        self.numberDots = 225
        self.dir = -1
        

    def setUp(self):
        self.window.colormode(255)
        self.getColors()
        self.draw.speed('fastest')
        
    def getColors(self):
        colors = colorgram.extract("Days-11-20\hirstPainting\pic.jpg",100)
        for c in colors:
            r = c.rgb.r
            g = c.rgb.g
            b = c.rgb.b
            newCol = (r,g,b)
            self.rgbColours.append(newCol)

    def move(self):
        self.draw.teleport(self.curPosX,self.curPosY)
    def paintSpot(self,color):
        self.draw.dot(20,color)

    def start(self):
        for i in range(self.numberDots):
            
            
            if i %15 == 0 and not i==0:
                self.curPosY+=50
                self.dir*=-1
                self.move()
            else:
                self.curPosX = (self.curPosX)+(50*self.dir)
                self.move()
            color = r.choice(self.rgbColours)
            self.paintSpot(color)
            
        self.window.exitonclick()

def main():
    paint = Paint()
    paint.setUp()
    paint.start()

if __name__ == "__main__":
    main()