import tkinter as tk
#Criando método para mostrar entradas


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
interface=tk.Tk()
#Interface Gráfica
tk.Label(interface,text="Primeiro Nome:").grid(row=0)
tk.Label(interface,text="Segundo Nome:").grid(row=1)
#Caixas de entrada
e1=tk.Entry(interface)
e2=tk.Entry(interface)
#Configurações de caixa
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
#Criando botões
tk.Button(interface,text="Quit",command=interface.quit).grid(row=3,column=0,sticky=tk.W,pady=4)   #Botão de Sair
tk.Button(interface,text='Show',command=show_entry_fields).grid(row=3,column=1,sticky=tk.,pady=4)   #Botão
interface.mainloop()
