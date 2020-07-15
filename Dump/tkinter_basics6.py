from tkinter import *
#from quitter import Quitter

def  fetch():
    print("Input => '%s'" % ent.get())
    ent.delete(0,END)


root = Tk()
root.resizable(False, False)
root.title("CIA chat")
root.geometry("200x67")
label1 = Label(text="Enter text here")
label1.pack(side=TOP)
ent = Entry(root)
#ent.insert(0, "Type words here")
ent.pack(side=TOP, fill=X)


ent.focus()
ent.bind("<Return>", (lambda event: fetch()))
#label1 = Label(text="Enter text here =>")
#label1.pack(side=LEFT)
btn = Button(root, text="Fetch", command=fetch)
btn.pack(side=TOP)
#Quitter(root).pack(side=RIGHT)
root.mainloop()
