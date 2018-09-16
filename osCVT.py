#CvT 2017 All rights reserved.
#Imports
import webbrowser
import pygame
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from datetime import datetime
from random import randint
from tkinter import Tk
import time
import pafy
from subprocess import call
import smtplib


pygame.init()
#vars
window = Tk()
c = Canvas(window, width=900, height=500)
window.title("CvT OS")
date = datetime.now()
music = pygame.mixer.Sound("dubstep.wav")
piano = pygame.mixer.Sound("sounds/piano.wav")
title = Label(window, text="Cvt OS", bg="green", fg="black")
title.pack(fill=X)
dateLabel = Label(window, text=date, fg="black")
dateLabel.pack(side=BOTTOM)
#functions
def ms():
    import ms
def paint():
    import paint
def quit():
    window.destroy()
    quit()
#Welcome message
message = "Welcome"
meh = Label(window, text=message, font='size, 40', fg="orange")
meh.pack()
#Functions
def change():
    text = askstring("CvT", "Whats the message?")
    meh.config(text=text)
changeb = Button(window, text="Change Message", command=change)
changeb.pack()
def notes():
    note = askstring("CvT", "Type your note in the area below.")
    noteL = Label(window, text=note, bg="orange", fg="white")
    noteL.pack(fill=X)
def google():
    webbrowser.open("https://www.google.com/")
def sound():
    url = askstring("CvT", "Give me the YouTube URL for your song!")
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    call(["cvlc", playurl])
def about():
    showinfo("CvT", "This is the CvT Open source OS version 1.3")
def CvTGames():
    import ms
def changep():
    with open("passwords.txt", "w") as saves:
        newp = askstring("CvT", "Whats your new password?")
        saves.write(newp)

def gitHub():
    messagebox.showinfo("CvT", "Feel free to commit code to the repo!")
    webbrowser.open("https://github.com/conniepocky/CvT-OS-1.0-")

def flood():
    import floodit

#menu vars
menu = Menu(window)
window.config(menu=menu)
subMenu = Menu(menu)
subMenu1 = Menu(menu)
subMenu2 = Menu(menu)
#menus
menu.add_cascade(label="System", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)
subMenu.add_command(label="Change Password", command=changep)
subMenu.add_command(label="About", command=about)
menu.add_cascade(label="Applications", menu=subMenu1)
subMenu1.add_command(label="Youtube Audio Player", command=sound)
subMenu1.add_command(label="CvT Notes", command=notes)
subMenu1.add_command(label="CvT Paint", command=paint)
subMenu1.add_command(label="Meteor Shower", command=CvTGames)
subMenu1.add_command(label="Google", command=google)
subMenu1.add_command(label="Flood It", command=flood)
menu.add_cascade(label="Developers", menu=subMenu2)
subMenu2.add_command(label="GitHub", command=gitHub)

#run

c.pack()
window.mainloop()
