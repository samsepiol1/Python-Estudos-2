idades=[]
nome=[]
for i in range(2):
    nome.append(input('Digite seu nome aqui').upper())
    idades.append(int(input("Digite a idade aqui:")))
    sexo=input("Digite seu Sexo F/M:").upper()
sexo_dois=input("Deseja ver informações sobre qual Sexo M/F/G(ambos)?").upper()
if(sexo_dois=='M'):
 for c in idades:
    for x in nome:
        y=0
        soma_das_idades=sum(idades)
        quantidade_idades=len(idades)
        media_das_idades=soma_das_idades/quantidade_idades

    for z in range(0):
        print(', '.join(nome))
        print('idades:{}'.format(idades))
        print("A média das idades é igual á {}".format(media_das_idades))

 print("A Maior idade entre os homens é de {} anos".format(max(idades)))
 print("A menor idade entre os homens é de {}".format(min(idades)))
elif(sexo_dois=='F'):
    for c in idades:
        for x in nome:
            y = 0
            soma_das_idades2=sum(idades)
            quantidade_idades2=len(idades)
            media_das_idades2=soma_das_idades2/quantidade_idades2


        for z in range(1):
            print(', '.join(nome))
            print("Idades: {}".format(idades))
            print("A media das idades é de {}".format(media_das_idades2))



    print("A Maior idade entre os homens é de: {} anos".format(max(idades)))
    print("A menor idade entre as mulher é de: {}".format(min(idades)))
elif(sexo_dois=='G'):
    print("A menor idade do grupo é de {}".format(min(idades)))
    soma_das_idades2 = sum(idades)
    quantidade_idades2 = len(idades)
    media_das_idades2 = soma_das_idades2 / quantidade_idades2

    soma_das_idades = sum(idades)
    quantidade_idades = len(idades)
    media_das_idades = soma_das_idades / quantidade_idades
    media_das_idades3=media_das_idades+media_das_idades2
    print("A média das idades é de {}".format(media_das_idades3))






















