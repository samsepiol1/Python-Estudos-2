from pygame import mixer
from tkinter import*
janela=Tk()
mixer.init()
var_teste = 'teste.mp3'
mixer.music.load(var_teste)
ed1=Entry(janela)
teste=ed1.get()
ed1.place(x=100,y=100)
if var_teste==teste:
    bt = Button(janela, text='Play', width=20,command=mixer.music.play())
    bt.place(x=100, y=150)
lb=Label(janela,text="Teste.mp3")
lb.place(x=100,y=200)
janela.geometry("400x300+200+200")
janela.mainloop()


