from tkinter import *

root=Tk()

# Create a menu button

mb=Menubutton(root,text="College")
mb.grid()

mb.menu=Menu(mb) # mb-->menubutton & menu is the function

mb["menu"]=mb.menu

Faculty=IntVar()
Student=IntVar()

mb.menu.add_checkbutton(label="Faculty",variable=Faculty)

mb.menu.add_checkbutton(label="Student",variable=Student)

mb.pack()

root.mainloop()
