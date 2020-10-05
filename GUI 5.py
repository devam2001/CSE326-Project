"""Write a program to create a tkinter window consisting of atleast 5 radiobutton for
providing the highest qualification of an employee. """

from tkinter import*
root = Tk()
def select():
    sel = "Highest Qualification of Employee is " + str(var.get())
    lbl.config(text=sel)

var = StringVar()
rd1 = Radiobutton(root, text="B.Tech ", variable=var, value=1, command=select)
rd1.pack(anchor=W)
rd2 = Radiobutton(root, text="M.Tech", variable=var, value=2, command=select)
rd2.pack(anchor=W)
rd3 = Radiobutton(root, text="PHD", variable=var, value=3, command=select)
rd3.pack(anchor=W)
rd4 = Radiobutton(root, text="B.Sc", variable=var, value=4, command=select)
rd4.pack(anchor=W)
rd5 = Radiobutton(root, text="M.Sc", variable=var, value=5, command=select)
rd5.pack(anchor=W)
rd6 = Radiobutton(root, text="HSC", variable=var, value=6, command=select)
rd6.pack(anchor=W)

lbl = Label(root)

lbl.pack(anchor=W)

root.mainloop()
