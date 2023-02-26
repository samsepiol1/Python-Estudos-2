colocado='Primeiro','Segundo','Terceiro', 'Quarto','Quinto'
controle=' '
media_saltos=0
contagem=0
total_saltos=0
lista_saltos=[]

while controle != '':
    nome=str(input('Coloque o nome do atleta:'))
    if nome=='':
        break
    for c in range(0,5):
        salto=float(input(f"{colocado[c]} Salto:"))
        total_saltos=total_saltos+salto
        media_saltos=total_saltos/5
        lista_saltos.append(salto)




print(nome)
print(lista_saltos)
print(media_saltos)




















