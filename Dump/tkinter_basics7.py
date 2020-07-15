from tkinter import *
import sys

root = Tk()
root.geometry("150x70")

def fetch():
    print(ent.get())
    ent.delete(0,END)


label_1 = Label(root, text="Enter text")
label_1.pack(side=TOP)
ent = Entry(root)
ent.pack(side=TOP, fill=X)

ent.bind("<Return>", lambda event: fetch())
but_1 = Button(root, text="FETCH", command = fetch)
but_1.pack(side=LEFT)
but_2 = Button(root, text="QUIT", command = sys.exit)
but_2.pack(side=RIGHT)
root.mainloop()

