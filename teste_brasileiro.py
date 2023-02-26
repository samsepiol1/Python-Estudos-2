import random
lista=['Pal']
Lista2=['Fla','flu ']
pontos=[3]
pontos_acumulado=[]
sorteio=random.choice(lista)
sorteio2=random.choice(Lista2)
print(sorteio)
for c in range(1):


    resultado4=random.randint(1,5)



for i in range(10):
    resultado5=random.randint(1,5)
    print('{}x{}'.format(resultado4,resultado5))
    if resultado5>resultado4:
        print('Acabou o jogo {} Venceu!!'.format(sorteio2))
    elif sorteio == lista[0] and resultado4 > resultado5:
        lista.append(3)
        print('Vitória do Palmeiras +3 pontos{}'.format(lista))
        resultado6=pontos*10
        resultado7=sum(resultado6)
print('Pontos Palmeiras',resultado7)








