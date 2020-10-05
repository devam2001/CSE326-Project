"""Write a program in python to create two different frames. Top frame will have
login form and bottom frame frame will have registration form"""

from tkinter import*
root = Tk()
root.geometry('450x200')
root.title('Login Form & Registration form')
def login():
    root1 = Tk()
    root1 = mainloop()
def register():
    root1 = Tk()
    root1 = mainloop()

usernameLabel = Label(root, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(root,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)

loginButton = Button(root, text="Login", command=login).grid(row=4, column=0)
_1 = Label(root, text="").grid(row=5, column=0)
a = Label(root, text="First Name").grid(row=6, column=0)
b = Label(root, text="Last Name").grid(row=7, column=0)
c = Label(root, text="Email Id").grid(row=8, column=0)
d = Label(root, text="Contact Number").grid(row=9, column = 0)
a1 = Entry(root).grid(row=6, column=1)
b1 = Entry(root).grid(row=7, column=1)
c1 = Entry(root).grid(row=8, column=1)
d1 = Entry(root).grid(row=9, column=1)

submitbutton = Button(root, text="Submit", command=register).grid(row=10, column=0)

root.mainloop()