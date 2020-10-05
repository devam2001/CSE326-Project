# Button and other imp function
# Alerting syntax for importing the Library
from tkinter import*
# Create a tkinter window
root = Tk()
# Set the dimension of the window
root.geometry("300x300")
# Create a Button
btn = Button(root, text="Please Click Me", bd="15", command=root.destroy)
# Set the Position of the button ---> pack, place, grid
btn.pack(side="top")
# Main Loop Execution
root.mainloop()
