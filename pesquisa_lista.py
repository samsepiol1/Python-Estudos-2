pessoas = ["Maria", "João", "Pedro," "Letícia", "Bruno", "Francisco"]

nome = input("Digite um nome")

x = 0

encontrado = False

while x<=len(pessoas)-1:
    if pessoas[x]==nome:
        encontrado = True
    x = x+1

if encontrado:
    print( nome,"está na lista")
else:
    print(nome,"Não está na lista")


