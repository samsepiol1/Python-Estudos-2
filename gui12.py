from tkinter import *
from arquivoteste import horario
from onibus_troco import troco1
import string
def Application():
    horario()
    return horario()
def Application1():
    troco1()
    return troco1()
def teste1():
    master=Tk()

    Label(master,text=open('teste.txt','r')).grid(row=0)

    mainloop()
    return mainloop()



master=Tk()
Label(master,text='Trampolim da vitoria').grid(row=0)
Button(master, text='Troco', command=Application1).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Horario', command=Application).grid(row=3, column=1, sticky=W, pady=4)
Button(master,text='Teste',command=teste1).grid(row=2,column=2,sticky=W,pady=4)
mainloop()

