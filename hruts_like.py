import re
contador = 0

nome = 'Tenho 3 máquinas para devolução e uma para troca, estou a meses tentando resolver mas n consigo, me falta o código de envio que não me fornecem, depois de já ligar várias vezes, está é a segunda vez que venho através deste canal solucionar, me informaram que minha conta é gerenciada, que iriam retirar no local a máquina, porém até agora nada, e recebo msg dizendo que serei descontado em 500 reais por cada maquina'

if re.search('\\btroca\\b', nome, re.IGNORECASE):
      for c in range(1):
          contador+=1
          print('Problema com Troca')
          print(contador)
else:
    print("Não é Troca")





