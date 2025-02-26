from assets.scripts.settings import *

class Program():
    def __init__(self):
        self.window = Tk()
        self.window.title(TITLE)
        self.window.config(padx=100,pady=50, bg=YELLOW)
        self.canvas = Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
        
        self.timer = None

        self.checkAmmount = 0
        self.curRep = 0
        self.workSec = math.trunc( WORK_MIN *60)
        self.longBreakSec = math.trunc(LONG_BREAK_MIN *60)
        self.shortBreakSec = math.trunc(SHORT_BREAK_MIN *60)

        self.loadData()




    def setup(self):
        self.title = Label(text="Timer", fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,'bold'))
        self.startBtn = Button(text="Start", command=self.startTimer)
        self.resetBtn = Button(text="Reset", command=self.reset)
        self.checkMarks = Label(text=("✔" * self.checkAmmount),fg=GREEN,bg=YELLOW)
        
        self.canvas.create_image(100, 112, image=self.tomatoImg)
        self.timerText = self.canvas.create_text(100,130,text="00:00" ,fill='white', font=(FONT_NAME,35,'bold'))
        
        self.createLayout()
        

        self.canvas.grid(column=1,row=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
    
    def createLayout(self):
        self.title.grid(column=1,row=0)
        self.startBtn.grid(column=0,row=2)
        self.resetBtn.grid(column=2,row=2)
        self.checkMarks.grid(column=1,row=3)

    def loadData(self):
        self.tomatoImg = PhotoImage(file=os.path.join(imgDir,"tomato.png"))
    

    
    def countDown(self,count):
        min = math.floor(count/60)
        sec = count % 60
        if sec < 10 :
            sec = f"0{sec}"
        if sec == 10:#Lift the window with a 10 seccond waring before it goes to fullscreen for break
            self.liftWindow()
        self.canvas.itemconfig(self.timerText, text=f'{min}:{sec}')
        if count > 0 :
            self.timer = self.window.after(1000,self.countDown,count - 1)
        else:
            self.startTimer()
            

    def startTimer(self):
        self.curRep +=1

        if self.curRep % 8 == 0:
            self.startBreakLong()
        elif self.curRep % 2 == 0:
            self.startBreakShort()
        else:
            self.window.attributes('-fullscreen',False) 
            self.title.config(text="Work",fg=GREEN)
            self.countDown(self.workSec)
    
    def liftWindow(self):
        self.window.lift()
        self.window.attributes('-topmost', True)
        self.window.after_idle(self.window.attributes, '-topmost', False)

    def reset(self):
        self.title.config(text="Timer",fg=GREEN)
        self.curRep = 0
        self.checkAmmount = 0
        self.checkMarks.config(text=("✔" * self.checkAmmount))
        self.canvas.itemconfig(self.timerText, text='00:00')
        self.window.after_cancel(self.timer)
        self.window.attributes('-fullscreen',False) 

    def startBreakLong(self):
        self.window.attributes('-fullscreen',True) 
        self.title.config(text="Break",fg=RED)
        self.countDown(self.longBreakSec)
        self.addCheck()
        self.liftWindow()

    def startBreakShort(self):
        self.window.attributes('-fullscreen',True) 
        self.title.config(text="Break",fg=PINK)
        self.countDown(self.shortBreakSec)
        self.addCheck()
        self.liftWindow()

    def addCheck(self):
        self.checkAmmount += 1
        self.checkMarks.config(text=("✔" * self.checkAmmount))

    def mainLoop(self):
        self.window.mainloop()
        
