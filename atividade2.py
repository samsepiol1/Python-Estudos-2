from random import randint

numero_de_jogos = 1

total_de_pontos = 0

while numero_de_jogos<=10:
    jogos_disputados_pontos = randint(0, 3)
    print(str(numero_de_jogos)+"\n"+"Jogo")
    numero_de_jogos = numero_de_jogos+1

    if jogos_disputados_pontos==3:
        total_de_pontos = total_de_pontos+jogos_disputados_pontos
        print("Vitoria")

    else:
        if jogos_disputados_pontos==1:
            total_de_pontos = total_de_pontos+jogos_disputados_pontos
            print("Empate")
print("Total de pontos:",total_de_pontos)


