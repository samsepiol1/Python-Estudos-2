lista_convidado={'Bruna','João','Paulo','Marcelo','Camargo','Matheus','Giovanna','Marcia'}
nome=str(input('Digite aqui o seu nome:')).capitalize()
if nome in lista_convidado:
    print('Seu nome está na lista de convidados')
else:
    print('Seu nome não está na lista, portanto não é um convidado')

