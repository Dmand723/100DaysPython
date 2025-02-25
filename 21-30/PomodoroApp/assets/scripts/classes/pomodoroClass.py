from assets.scripts.settings import *

class Program():
    def __init__(self):
        self.window = Tk()
        self.window.title(TITLE)




    def setup(self):
        self.tomatoImg = PhotoImage(file="assets/imgs/tomato.png")
        self.canvas = Canvas(width=200,height=224)
        self.canvas.create_image(100, 112, image=self.tomatoImg)

    def mainLoop(self):
        self.window.mainloop()
