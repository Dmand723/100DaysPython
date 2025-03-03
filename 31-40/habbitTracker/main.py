import requests 
import os
from dotenv import load_dotenv
import datetime as dt
from tkinter import *
from tkinter import messagebox
class PixleTracker():
    def __init__(self):
        load_dotenv()

        self.TOKEN = os.getenv('TOKEN')
        self.USERNAME = os.getenv('PIXELUSERNAME')

        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_endpoint = f'{self.pixela_endpoint}/{self.USERNAME}/graphs'
        self.HEADERS = {
            'X-USER-TOKEN': self.TOKEN
        }

        self.entrys = []
        self.allWidgets = []
        self.entryWitdh = 30 
        self.todaysDate = dt.date.today().strftime("%Y/%m/%d")
        
        self.root = Tk()
        self.root.config(padx=80,pady=80)
        self.root.title('Pixle Tracker')

    
        
        self.createWidgetsMain()
        self.createLayoutMain()
        self.root.mainloop()


    
    def createWidgetsMain(self):
        #Create New Graph Button
        self.newGraphBtn = Button(text='New Graph', command=self.newGraphWindow)
        self.allWidgets.append(self.newGraphBtn)

        #Update Graph graphID
        self.graphIdLbl = Label(text="Graph Id:")
        self.allWidgets.append(self.graphIdLbl)
        self.graphIdEntry = Entry(width=self.entryWitdh)
        self.graphIdEntry.focus()
        self.entrys.append(self.graphIdEntry)
        self.allWidgets.append(self.graphIdEntry)

        #Update Graph Date:
        self.graphDateLbl = Label(text="Date (yyyy/mm/dd):")
        self.allWidgets.append(self.graphDateLbl)

        self.graphDateEntry = Entry(width=self.entryWitdh)
        self.graphDateEntry.insert(0,self.todaysDate)
        self.allWidgets.append(self.graphDateEntry)
        self.entrys.append(self.graphDateEntry)

        #Update Graph Quantity:
        self.graphQuantityLbl = Label(text="Update Ammount:")
        self.allWidgets.append(self.graphQuantityLbl)

        self.graphQuantityEntry = Entry(width=self.entryWitdh)
        self.allWidgets.append(self.graphQuantityEntry)
        self.entrys.append(self.graphQuantityEntry)

        #Update Submit Btn
        self.graphSubmitBtn = Button(text="Update Graph",command=self.onSubmitMain)
        self.allWidgets.append(self.graphSubmitBtn)
        
        
        
        
    
    def createLayoutMain(self):
        #Create New Graph Button
        self.newGraphBtn.grid(row=0,column=1)
        
        #Update Graph GraphId
        self.graphIdLbl.grid(row=1,column=0)
        self.graphIdEntry.grid(row=1,column=1)
        

        #Update Graph Date
        self.graphDateLbl.grid(row=2,column=0)
        self.graphDateEntry.grid(row=2,column=1)

        #Update Graph Quantity
        self.graphQuantityLbl.grid(row=3,column=0)
        self.graphQuantityEntry.grid(row=3,column=1)

        #Update Submit Btn
        self.graphSubmitBtn.grid(row=4,column=1)
        
        

    def createWidgetsNew(self):
        #new id:
        self.newGraphIdLbl = Label(text="New Graph Id:")
        self.allWidgets.append(self.newGraphIdLbl)

        self.newGraphIdEntry = Entry(width=self.entryWitdh)
        self.entrys.append(self.newGraphIdEntry)
        self.allWidgets.append(self.newGraphIdEntry)

        #new Name:
        self.newGraphNameLbl = Label(text="New Graph Name:")
        self.allWidgets.append(self.newGraphNameLbl)

        self.newGraphNameEntry = Entry(width=self.entryWitdh)
        self.entrys.append(self.newGraphNameEntry)
        self.allWidgets.append(self.newGraphNameEntry)

        #new Unit
        self.newGraphUnitLbl = Label(text="New Graph Unit:")
        self.allWidgets.append(self.newGraphUnitLbl)

        self.newGraphUnitEntry = Entry(width=self.entryWitdh)
        self.entrys.append(self.newGraphUnitEntry)
        self.allWidgets.append(self.newGraphUnitEntry)

        #new Type:
        self.newGraphTypeLbl = Label(text="int or float?:")
        self.allWidgets.append(self.newGraphTypeLbl)

        self.newGraphTypeEntry = Entry(width=self.entryWitdh)
        self.entrys.append(self.newGraphTypeEntry)
        self.allWidgets.append(self.newGraphTypeEntry)
        
        #new Color:
        self.newGraphColorLbl = Label(text="New Graph color")
        self.allWidgets.append(self.newGraphColorLbl)

        self.newGraphColorEntry = Entry(width=self.entryWitdh)
        self.allWidgets.append(self.newGraphColorEntry)
        self.entrys.append(self.newGraphColorEntry)

        #new Submit Button
        self.newGraphSubmitBtn = Button(text="Submit", command=self.onSubmitNew)
        self.allWidgets.append(self.newGraphSubmitBtn)

    def createLayoutNew(self):
        #New Id
        self.newGraphIdLbl.grid(row=0,column=0)
        self.newGraphIdEntry.grid(row=0,column=1)

        #New Name
        self.newGraphNameLbl.grid(row=1,column=0)
        self.newGraphNameEntry.grid(row=1,column=1)

        #New Unit
        self.newGraphUnitLbl.grid(row=2,column=0)
        self.newGraphUnitEntry.grid(row=2,column=1)

        #New Type
        self.newGraphTypeLbl.grid(row=3,column=0)
        self.newGraphTypeEntry.grid(row=3,column=1)

        #New Color
        self.newGraphColorLbl.grid(row=4,column=0)
        self.newGraphColorEntry.grid(row=4,column=1)

        #New Submit Button
        self.newGraphSubmitBtn.grid(row=5,column=1)


    def mainloop(self):
        self.root.mainloop()

    def newGraphWindow(self):
        self.clearWindow()
        self.createWidgetsNew()
        
        self.createLayoutNew()
        
        
    def createNewGraph(self,config):
        
        res = requests.post(url=self.graph_endpoint,json=config,headers=self.HEADERS)
        if res.status_code == 404:
            messagebox.showerror('No Page Found',f"No Page {self.graph_endpoint} found")
        elif res.status_code == 400:
            messagebox.showerror("Reqest Error",res.text)
        else:
           messagebox.showinfo("Succsess","Graph Created Succsessfully")

    def createNewPixle(self,graphID:str,req):
        post_pixle_endpoint = f'{self.graph_endpoint}/{graphID}'

        res = requests.post(url=post_pixle_endpoint,json=req,headers=self.HEADERS)
        if res.status_code == 404:
            messagebox.showerror('No Graph Found',"No Graph With That Id Found")
        elif res.status_code == 400:
            messagebox.showerror("Reqest Error","Username or Token is incorrect")
        else:
            messagebox.showinfo("Succsess","Graph Updated Succsessfully")
    
    def clearWindow(self):
        for e in self.allWidgets:
            e.destroy()
        self.allWidgets.clear()
        self.entrys.clear()

    def onSubmitNew(self):
        req = {
            "id":self.newGraphIdEntry.get(),
            "name":self.newGraphNameEntry.get(),
            "unit":self.newGraphUnitEntry.get(),
            "type":self.newGraphTypeEntry.get(),
            "color":self.newGraphColorEntry.get()
        }
        self.createNewGraph(req)
        self.clearWindow()
        self.createWidgetsMain()
        self.createLayoutMain()

        
    
    def onSubmitMain(self):
        

        req = {
            'date':self.graphDateEntry.get().replace('/',''),
            'quantity':self.graphQuantityEntry.get()
        }
        self.createNewPixle(self.graphIdEntry.get(),req)
        for item in self.entrys:
            item.delete(0,END)
        self.graphDateEntry.insert(0,self.todaysDate)
        self.graphIdEntry.focus()

def main():
    program = PixleTracker()
 

main()



