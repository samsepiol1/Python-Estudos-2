c=0
x=0
media=0
idade_lista=[]
lista_mulher=[]
while c==0 or x==0:
    nome = input('Digite aqui o seu nome:')
    sexo = input('Insira o seu sexo:').upper()
    idade = int(input('Insira sua idade:'))
    idade_lista.append(idade)
    c = int(input('0-Continuar\n1-Sair'))
    x=x+1
    media1=sum(idade_lista)/x
    print('Quantidade de pessoas cadastradas:{}'.format(x))
    print('A media das idade é de {}'.format(media1))
    if sexo=='F':
        lista_mulher.append(nome)
        print(lista_mulher)
    elif idade>media1:
        dicionario_dados={'Nome':nome,'Sexo':sexo,'Idade':idade_lista}
        for k,v in dicionario_dados.items():
            print(f'{k} {v}')
dicionario_dados={'Nome':nome,'Sexo':sexo,'Idade':idade_lista}
print(dicionario_dados)
