#Imports
from guizero import App, Text, TextBox
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
#Vars
app = App("CvT Writers")
title = Text(app, text="My Book.", size=25, color="purple")
story = TextBox(app, width=60)
story1 = TextBox(app, width=60)
story2 = TextBox(app, width=60)
story3 = TextBox(app, width=60)
#Run
app.display()
