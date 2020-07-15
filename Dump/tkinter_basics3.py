from tkinter import *
import sys

root = Tk()
root.resizable(False, False)
root.geometry("100x50")

def yes():
    print("Hello retard niggerfaggot")

widget1 = Label(text="Are you gay?")
widget1.pack(side=TOP)
widget2 = Button(root, text="YES", command=yes)
widget2.pack(side=LEFT)
widget3 = Button(root, text="YES", command=yes)
widget3.pack(side=RIGHT)
root.mainloop()
