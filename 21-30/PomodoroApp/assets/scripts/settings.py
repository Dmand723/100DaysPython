#----------------------------- Imports --------------------------------- #
from tkinter import *
import math
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TITLE = 'Time to study'
WIDTH = 800
HEIGHT = 800

mainDir = os.path.dirname(__file__)
gameDir = mainDir.replace("\\assets\\scripts", "")
assetsDir = os.path.join(gameDir,"assets")
scriptsDir = os.path.join(assetsDir,"scripts")
classesDir = os.path.join(scriptsDir,"classes")
imgDir = os.path.join(assetsDir,"imgs")