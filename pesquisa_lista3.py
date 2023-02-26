pessoas = ["Maria", "João", "Pedro," "Letícia", "Bruno", "Francisco"]
nome = input("Digite um nome")

for x in pessoas:
    if x==nome:
        encontrado=True
if encontrado:
    print("Nome está na lista")
else:
    print("Nome não está na lista")
