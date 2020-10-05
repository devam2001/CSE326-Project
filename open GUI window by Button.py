from tkinter import *

root=Tk()

def new():
    roott=Tk()
    roott.mainloop()

btn=Button(root,text="Next Window",command=new)

btn.pack()

root.mainloop()