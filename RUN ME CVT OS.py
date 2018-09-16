#passwords
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter import Tk
import tkinter
tk = Tk()
tk.withdraw()

title = Label(tk, text="Sign in", bg="green", fg="black")
title.pack(fill=X)
with open("passwords.txt", "r") as saves:
    password = saves.read()
    guess = askstring("CvT", "Whats your password?")
    
    if guess == password:
        import osCVT
        quit()
    else:
        quit()
tk.pack()
