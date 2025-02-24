from scripts.settings import *  
class Snake():
    def __init__(self):
        self.snakeBody = []
        self.bodyAmount = 3
        self.curDirection = 'right'
        self.movedist = 20
        for i in range(self.bodyAmount):
            self.createSegment((i*-20,0))
        self.snakeHead = self.snakeBody[0]

    def createSegment(self,pos:tuple):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(pos)
        self.snakeBody.append(segment)

    def extend(self):
        #add a new segment to the snake.
        self.createSegment(self.snakeBody[-1].position()) 

    def move(self):
        for seg_num in range(len(self.snakeBody)-1, 0,-1,):
            newX = self.snakeBody[seg_num-1].xcor()
            newY = self.snakeBody[seg_num-1].ycor()
            self.snakeBody[seg_num].goto(newX,newY)
        self.snakeHead.forward(self.movedist)
        
    def up(self):
        if not self.curDirection == 'down':    
            self.snakeHead.setheading(90)
            self.curDirection = 'up'

    def down(self):
        if not self.curDirection == 'up': 
            self.snakeHead.setheading(270)
            self.curDirection = 'down'

    def right(self):
        if not self.curDirection == 'left':
            self.snakeHead.setheading(0)
            self.curDirection = 'right'

    def left(self):
        if not self.curDirection == 'right':
            self.snakeHead.setheading(180)
            self.curDirection = 'left'