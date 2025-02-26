from tkinter import *
from tkinter import messagebox
import os
import random as r
import pyperclip 
import json

mainDir = os.path.dirname(__file__)
EMAIL = 'dawson.simmons723@gmail.com'
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
        self.entrys = []
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
        self.entrys.append(self.webEntry)
        self.emailEntry = Entry(width=35)
        self.entrys.append(self.emailEntry)
        self.emailEntry.insert(0, EMAIL)
        self.passEntry = Entry(width=35)
        self.entrys.append(self.passEntry)

        self.genBtn = Label(text="🎲",width=3)
        self.genBtn.bind("<Button-1>", func=self.randomizePassword)
        self.searchBtn = Label(text='🔎',width=3)
        self.searchBtn.bind("<Button-1>", func=self.handleSearch)
        
        self.addBtn = Button(text="Add",width=35, command=self.savePass)

    def createLayout(self):
        self.webLabel.grid(row=1,column=0)
        self.webEntry.grid(row=1,column=1,columnspan=2)

        self.emailLabel.grid(row=2,column=0) 
        self.emailEntry.grid(row=2,column=1,columnspan=2)

        self.passLabel.grid(row=3,column=0) 
        self.passEntry.grid(row=3,column=1,columnspan=2)

        self.searchBtn.grid(row=1,column=3)
        self.genBtn.grid(row=3,column=3)
        self.addBtn.grid(row=5,column=1)
        
    def loadData(self):
        logoDir = os.path.join(mainDir,"logo.png")
        self.textDir = os.path.join(mainDir,"passwords.json")
        self.img = PhotoImage(file=logoDir)

    def randomizePassword(self, catch = None):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '*']   
        numberLetters = r.randint(8,10)
        numberSymbols = r.randint(2,4)
        numberNumbers = r.randint(2,4)
        password = []
        for i in range(numberLetters):
            password.append(str(letters[r.randint(0,len(letters)-1)]))
        for i in range(numberSymbols):
            password.append(str(symbols[r.randint(0,len(symbols)-1)]))
        for i in range(numberNumbers):
            password.append(str(numbers[r.randint(0,len(numbers)-1)]))
        r.shuffle(password)
        password = ''.join(password)
        self.passEntry.delete(0,END)
        self.passEntry.insert(0,password)
        pyperclip.copy(password)
        

    def savePass(self):
        
        website = self.webEntry.get()
        email = self.emailEntry.get()
        password = self.passEntry.get()
        newData = {website:{
            "email": email,
            "password":password
        }}
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showwarning("Stupid Boy","Don't leave any of the fields empty")
        else:
            isCorrect = messagebox.askyesno("Are you sure",f"is this Data correct?: \nWebsite: {website}\nEmail/Username: {email}\nPassword:{password}")
            if isCorrect:
                try:
                    with open(self.textDir,'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    with open(self.textDir,'w') as file:
                        json.dump(newData,file,indent=4)
                else:
                    data.update(newData)
                    with open(self.textDir, 'w') as file:
                        json.dump(data,file,indent=4)
                finally:
                    file.close()
                    self.clearFeilds()
            else:
                pass

    def clearFeilds(self):
        for e in self.entrys:
            e.delete(0,END)
        self.emailEntry.insert(0,EMAIL)
    
    def handleSearch(self,catch = None):
        try:
            with open(self.textDir,'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Not Found", message="No password file found please create a password or recover password file")
        else:
            try:
                foundData = data[self.webEntry.get()]
            except KeyError:
                messagebox.showwarning('Not Found',"No passwords found for that website")
            else:
                messagebox.showinfo('Login',f'Email/username: {foundData['email']}\nPassword: {foundData['password']}')
            file.close()
        



def main():
    program = Program()


main()