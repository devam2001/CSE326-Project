from tkinter import *

root = Tk()

def select():
    sel = "Your selected option is:" + str(var.get())
    lbl.config(text=sel)

var=IntVar()

rd1 = Radiobutton(root, text="Option 1",variable=var, value=1, command=select)

rd1.pack(anchor=W)

rd2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=select)

rd2.pack(anchor=W)

rd3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=select)

rd3.pack(anchor=W)


lbl = Label(root)

lbl.pack(anchor=W)

root.mainloop()
