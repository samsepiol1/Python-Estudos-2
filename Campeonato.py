import random
times=['Corithians','Palmeiras','Atlético-MG','Botafogo','São Paulo','Bahia','Santos','Internacional','Vasco','Grêmio','Flamengo']
times2=['Cruzeiro','Goias','Ceará','Csa','Fortaleza','Paranaense','Avái','Chapeco','Cruzeiro']
pontos=[3]
resultado7=0
sorteio=random.choice(times)
sorteio2=random.choice(times2)
print(sorteio)
print('X')
print(sorteio2)
for c in range(1):


    resultado4=random.randint(1,5)



for i in range(1):
    resultado5=random.randint(1,5)
    print('{}x{}'.format(resultado4,resultado5))
    if resultado5>resultado4:

        print('Acabou o jogo {} Venceu!!'.format(sorteio2))
    else:
        print('Acabou o jogo {} Venceu !!'.format(sorteio))
    if sorteio == times[0] and resultado5>resultado4:
        times.append(3)
        print('Vitória do Cori +3 pontos{}'.format(pontos))
        resultado6=pontos*1
        resultado7=sum(resultado6)
    elif sorteio==times[1] and resultado5>resultado4:
        times.append(3)
        print('Vitoria do palmeiras +3 pontos{}'.format(pontos))
print('Pontos Corinthians',resultado7)














