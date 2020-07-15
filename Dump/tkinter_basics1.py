from tkinter import *
import sys
root = Tk()

def handler(name):
    print(name)


widget = Label(root,text="Click this nigger --->")
widget.pack(side=LEFT)
widget2 = Button(root, text="Close", command=(lambda : handler("spam")))
widget2.pack(side=TOP,expand=YES, fill=Y)
root.mainloop()
