from tkinter import *
top = Tk()
L1 = Label(top, text="User Name")
L2=Label(top,text="Password")
L1.pack( side = LEFT)
L2.pack(side=RIGHT)
E1 = Entry(top, bd =5)
E2=Entry(top,bd=4)
E1.pack(side = RIGHT)
E2.pack(side=LEFT)
top.mainloop()
