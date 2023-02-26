from random import *

numero_usario = int(input("Digite um número entre 0 e 20"))

gerado = randint(0,21)

while gerado!=numero_usario:
    if numero_usario>gerado:
        print("O número que você digitou é menor")
    else:
        print("O número digitado é maior")
    numero_usario = int(input('Digite um número entre 0 e 20'))
print("Parabéns você acertou")