""" To Create a label for Student """
from tkinter import*
root = Tk()
l1 = Label(root, text="Name ")
l2 = Label(root, text="Roll ")
l3 = Label(root, text="Course ")
l4 = Label(root, text="Registration No. ")
l5 = Label(root, text="Ph. No. ")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)
l5.grid(row=4, column=0)

e1 = Entry(root, bd=10)
e1.grid(row=0, column=1)
e2 = Entry(root, bd=10)
e2.grid(row=1, column=1)
e3 = Entry(root, bd=10)
e3.grid(row=2, column=1)
e4 = Entry(root, bd=10)
e4.grid(row=3, column=1)
e5 = Entry(root, bd=10)
e5.grid(row=4, column=1)
root.mainloop()
"""#Label and Entrybox

from tkinter import *

root=Tk()

#Create a label

lbl=Label(root,text="User Name")

#lbl.pack(side=LEFT)
lbl.grid(row=1,column=0)


#Create a entrybox--textbox

ent=Entry(root,bd=10)

#ent.pack(side=RIGHT)
ent.grid(row=1,column=1)

root.mainloop()

#Write a program to get atleast 5 attributes of the student using proper label & entry box. Also add one button along with it."""
