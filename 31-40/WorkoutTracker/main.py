import requests
from dotenv import load_dotenv
import os
from datetime import datetime as dt
from tkinter import *
from tkinter import messagebox

class WorkoutTraker():
    def __init__(self):
        self.GENDER = 'male'
        self.WEIGHT_KG = 73
        self.HEIGHT_CM = 173
        self.AGE = 18

        load_dotenv()
        self.APP_ID = os.getenv('APP_ID')
        self.API_KEY = os.getenv('API_KEY')
        self.TOKEN = os.getenv('TOKEN')

        self.exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.sheet_endpoint = 'https://api.sheety.co/9641387e59dfa1814de392f6f7fa6695/myWorkoutsPython/workouts'
        self.headers = {
            'x-app-id': self.APP_ID,
            'x-app-key':self.API_KEY
        }
        
        self.basic_headers = {
            'Authorization': f"Bearer {self.TOKEN}"
        }

        self.entrys = []

        self.createRoot()
        self.createWidgets()
        self.createLayout()
        self.root.mainloop()
    
    def createRoot(self):
        self.root = Tk()
        self.root.config(padx=80,pady=80)
        self.root.title('Workout Tracker')


    def createWidgets(self):
        self.title = Label(text='Enter a new workout')

        self.newWorkoutLbl = Label(text="Tell me which exercises you did:")
        self.newWorkoutEntry = Entry(width=80)
        self.entrys.append(self.newWorkoutEntry)

        self.submitBtn = Button(text="Submit" ,command=self.addWorkout)



    def createLayout(self):
        self.title.grid(row=0,column=1)

        self.newWorkoutLbl.grid(row=1,column=0)
        self.newWorkoutEntry.grid(row=1,column=1)
        
        self.submitBtn.grid(row=3,column=1)

    def addWorkout(self):
        exerciseText = self.newWorkoutEntry.get()
        req = {
            "query": exerciseText,
            "gender": self.GENDER,
            "weight_kg": self.WEIGHT_KG,
            "height_cm": self.HEIGHT_CM,
            "age": self.AGE
        }
        





        res = requests.post(self.exercise_endpoint,json=req,headers=self.headers)
        result = res.json()

        today_date = dt.now().strftime("%d/%m/%Y")
        now_time = dt.now().strftime("%X")




        for exercise in result["exercises"]:
            sheet_inputs = {
                "workout": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            #Basic Authentication
            sheet_response = requests.post(self.sheet_endpoint,json=sheet_inputs,headers=self.basic_headers)

            messagebox.showinfo("Succsess","Data added succsessfully")
            self.newWorkoutEntry.delete(0,END)

WorkoutTraker()