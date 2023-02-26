import random
def palavra_correta(palavraum,palavradois):
    if palavraum=='s':
        palavra=input('Digite aqui a palavra').lower()
    if palavra==sorteio:
        print('Parabens! a palavra correta era: {}'.format(sorteio))
    return

letra=input('Digite aqui uma letra:')
elementos=['paz','amor','fraternidade']
sorteio=random.choice(elementos)
palavra=''
palavra2=''
if letra in sorteio:
   print('Existe essa letra na palavra')
   print('A palavra tem {} letra'.format(len(sorteio)))
   print('Essa palavra aparece {} na palavra'.format(sorteio.count(letra)))
   palavra=input('Já sabe qual é a palavra S/N')
   palavra_correta(palavra,palavra2)
else:
    while letra not in sorteio:
        print('Letra não existe')
        letra=input('Digite aqui outra letra')
        if letra in sorteio:
            palavra2=''
            print('Existe essa letra na palavra')
            print('A palavra tem {} letra'.format(len(sorteio)))
            print('Essa palavra aparece {} na palavra'.format(sorteio.count(letra)))
            palavra = input('Já sabe qual é a palavra S/N')
            palavra_correta(palavra,palavra2)



















