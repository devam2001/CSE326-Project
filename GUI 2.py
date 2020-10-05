import tkinter
from tkinter import messagebox

root = tkinter.Tk()


def hello():
    messagebox.showinfo("Hello Python", "This Is My First Message box")


btn = tkinter.Button(root, text="Click Me", command=hello)
btn.pack()
root.mainloop()
