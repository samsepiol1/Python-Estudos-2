from random import randint
def numero_aleatorio():
    lista=[]
    vezes=input('Quantos numeros você deseja:')
    while len(lista)<int(vezes):
        numero=0

        for i in range(randint(2,10)):
            numero+=randint(2,10)
            numero_string_trans=str(numero)

        if numero not in lista:
            lista.append(numero_string_trans)
            print(''.join(lista))
    return lista
#Testar Função
numero_aleatorio()
def inverte_palavras():
    palavra=input('Digite aqui qualquer palavra:')
    nova_palavra=list(palavra)
    nova_palavra.reverse()
    palavra_invertida=''.join(nova_palavra)
    return nova_palavra
#Testar função
inverte_palavras()



