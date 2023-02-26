import random
nome1=str(input('Primeiro Aluno:'))
nome2= str (input('Segundo Aluno:'))
nome3=str (input('Terceiro Aluno:'))
nome4=str(input ('Quarto Aluno:'))
nomes_sorteio=[nome1,nome2,nome3,nome4]
escolhido=random.choice(nomes_sorteio)
print('o Escolhido no sorteio foi igual a {}'.format(escolhido))






