lista_numero = [1,2,3,4,5]
numero = int(input('Digite aqui um número'))
for x in lista_numero:
    if x ==numero:
        encontrado=True
if encontrado:
    print('Número Encontrado')
else:
    print('Numero não encontrado ')