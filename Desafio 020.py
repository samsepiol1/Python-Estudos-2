from random import shuffle
nome1=str(input('Primeiro Aluno:'))
nome2=str(input('Segundo Aluno:'))
nome3=str(input('Terceiro Aluno:'))
nome4=str(input('Quarto nome:'))
lista_sorteio=[nome1,nome2,nome3,nome4]
shuffle(lista_sorteio)
print('A ordem de apresentação vai ser')
print(lista_sorteio)



