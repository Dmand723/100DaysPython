from tkinter import *
import os

mainDir = os.path.dirname(__file__)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

class Program():
    def __init__(self):
        self.root = Tk()
        self.root.title('Password Manger')
        self.root.config(padx=50, pady=50)
        self.canvas = Canvas(height=200,width=300)

        self.loadData()
        self.createWidgets()
        
        self.createLayout()
        self.canvas.grid(row=0,column=1)
        self.webEntry.focus()
        self.root.mainloop()

    

    def createWidgets(self):
        self.logoImg = self.canvas.create_image(100,100,image=self.img)
        self.webLabel = Label(text="Website:")
        self.emailLabel = Label(text="Email/Username:")
        self.passLabel = Label(text="Password:")
        self.webEntry = Entry(width=35)
        self.emailEntry = Entry(width=35)
        self.passEntry = Entry(width=35)
        self.genBtn = Label(text="🎲",width=3)
        self.genBtn.bind("<Button-1>", func=self.randomizePassword)
        self.addBtn = Button(text="Add",width=35, command=self.savePass)

    def createLayout(self):
        self.webLabel.grid(row=1,column=0)
        self.webEntry.grid(row=1,column=1,columnspan=2)

        self.emailLabel.grid(row=2,column=0) 
        self.emailEntry.grid(row=2,column=1,columnspan=2)

        self.passLabel.grid(row=3,column=0) 
        self.passEntry.grid(row=3,column=1,columnspan=2)

        self.genBtn.grid(row=3,column=3)
        self.addBtn.grid(row=5,column=1)
        
    def loadData(self):
        print(mainDir);
        logoDir = os.path.join(mainDir,"logo.png")
        print(logoDir)
        self.img = PhotoImage(file=logoDir)

    def randomizePassword(self, catch):
        print("Random")

    def savePass(self):
        website = self.webEntry.get()
        email = self.emailEntry.get()
        password = self.passEntry.get()
        textDir = os.path.join(mainDir,"passwords.txt")
        file = open(textDir,'a')
        file.write(f'{website} | {email} | {password}')
        file.close()
        self.clearFeilds()

    def clearFeilds(self):
        pass


def main():
    program = Program()


main()