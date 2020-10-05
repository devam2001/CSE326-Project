#Scale

from tkinter import * # Library

root=Tk() # window

def select():
    selection= "Value selected is:"+ str(var.get())
    lbl.config(text=selection)

var=IntVar() #dynamic variable datatype

scale=Scale(root,variable=var) # Scale is created
scale.pack() # set position

btn=Button(root,text="Get the value of the sacle",command=select) #btn for value selection
btn.pack()# set position

lbl=Label(root)# value selection will be displayed
lbl.pack()# set position

root.mainloop() # executing the fun for infinte no of time
