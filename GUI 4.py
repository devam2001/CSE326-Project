# Label and EntryBox
from tkinter import*
root = Tk()
# Create Label
lbl = Label(root, text="User Name")
lbl.pack(side=LEFT)
# Create a entrybox --textbox
ent = Entry(root, bd=10)
ent.pack(side=RIGHT)
root.mainloop()
