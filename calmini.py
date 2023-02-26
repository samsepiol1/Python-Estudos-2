from tkinter import*
from pygame import mixer
janela=Tk()
def bt_click():
    mixer.init()
    print("Executando...")
    num1 = str(ed1.get())
    mixer.music.load(num1)
    mixer.music.play()
    lb['text']=num1
def bt_click2():
    mixer.init()
    print('Pausando...')
    mixer.music.pause()

ed1=Entry(janela)
ed1.place(x=100,y=100)
bt=Button(janela,text="Play",width=20,command=bt_click)
bt.place(x=100,y=150)
lb=Label(janela,text=ed1)
lb.place(x=100,y=200)
janela.geometry("400x300+200+200")
janela.mainloop()