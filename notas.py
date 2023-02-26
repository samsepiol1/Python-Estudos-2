lista_notas=[]
for c in range(1,5):
    n=int ((input('Digite aqui 4 notas')))
    lista_notas.append(n)
    soma=sum(lista_notas)
    media=soma/c
print('As notas são iguais a{} e a média entre elas é igual a {}'.format(lista_notas,media))





