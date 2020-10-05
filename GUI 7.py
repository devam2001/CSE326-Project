from tkinter import *

root=Tk()

btn1=Button(root,text="1",padx=15,pady=15,font=("Times New Roman",25,"bold"),height=3,width=3,fg="black",bg="yellow",command=lambda:btnclick(1))
btn1.grid(row=1,column=1)

btn2=Button(root,text="2",padx=15,pady=15,font=("Times New Roman",25,"bold"),height=3,width=3,fg="black",bg="yellow",command=lambda:btnclick(2))
btn2.grid(row=1,column=2)

btn3=Button(root,text="3",padx=15,pady=15,font=("Times New Roman",25,"bold"),height=3,width=3,fg="black",bg="yellow",command=lambda:btnclick(3))
btn3.grid(row=1,column=3)

btn4=Button(root,text="4",padx=15,pady=15,font=("Times New Roman",25,"bold"),height=3,width=3,fg="black",bg="yellow",command=lambda:btnclick(4))
btn4.grid(row=1,column=4)


root.mainloop()
