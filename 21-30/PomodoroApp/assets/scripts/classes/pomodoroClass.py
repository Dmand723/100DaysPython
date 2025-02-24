from assets.scripts.settings import *

class Program():
    def __init__(self):
        self.window = Tk()
        self.window.title("Time To study")




    def setup(self):
        self.tomatoImg = PhotoImage(file="assets/imgs/tomato.png")
        self.canvas = Canvas(width=200,height=224)
        self.canvas.create_image(100, 112, image='')

    def mainLoop(self):
        self.window.mainloop()
