# Canvas
from tkinter import *

root = Tk()

# Empty Canvas
cv = Canvas(root, bg="blue", height=300, width=300)
cv.pack()
# Create Arc
coordinate = 35, 100, 100, 60
arc = cv.create_arc(coordinate, start=0, extent=150, fill="red")
root.mainloop()
