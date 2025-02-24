from scripts.settings import *
from scripts.classes.snakeClass import Snake
from scripts.classes.foodClass import Food
from scripts.classes.scoreBoardClass import ScoreBoard
class Game():
    def __init__(self):
        self.window = Screen()
        self.window.setup(width=SCREEN_W, height=SCREEN_H)
        self.window.bgcolor(BG_COLOR)
        self.window.title(TITLE)
        self.window.tracer(0)
        self.window.listen()
    


        

          
    def setup(self):# Setup Start Game   
        self.snake = Snake()
        self.food = Food()
        self.scoreBoard = Turtle()
        

        self.score = 0
        self.scoreBoard = ScoreBoard(self.score)

        self.window.onkey(self.snake.up,'Up')
        self.window.onkey(self.snake.down,'Down')
        self.window.onkey(self.snake.left,'Left')
        self.window.onkey(self.snake.right,'Right')
        self.window.onkey(self.endGame,"Escape")
        self.playing = True

    def update(self):
        self.window.update()
        wait(.1)
        self.snake.move()
        self.detectCollision()
       
        
    def detectCollision(self):
         #detect collision with food
        if self.snake.snakeHead.distance(self.food) < 15:
            self.colideWithFood()
        #Detect collision with wall X
        if self.snake.snakeHead.xcor() >280 or self.snake.snakeHead.xcor() < -280:
            self.endGame()
        #Dectect collision with wall Y
        if self.snake.snakeHead.ycor() >280 or self.snake.snakeHead.ycor() < -280:
             self.endGame()

        #Detect collision with tail
        for segment in self.snake.snakeBody[1:]:
            if self.snake.snakeHead.distance(segment) <10:
                self.endGame()


    def colideWithFood(self):
        
        self.food.move()
        self.snake.extend()
        self.addScore()

    def addScore(self):
        self.score +=1
        self.scoreBoard.updateScore(self.score)


    def mainLoop(self):
        while self.playing: 
            self.update()
        
        self.window.exitonclick()

    def endGame(self):
        self.playing = False
        self.scoreBoard.gameOver()