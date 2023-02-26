pro1=float(input('Qual o preço do primeiro produto? R$'))
pro2=float(input('Qual o preço do segundo produto? R$'))
pro3=float(input('Qual o preço do terceiro produto? R$'))
if pro1<pro2 and pro1<pro3:
    print('Você deveria comprar o primeiro produto R$'.format(pro1))
elif pro2<pro1 and pro2<pro3:
    print('Você deveria comprar o segundo produtoR$'.format(pro2))
elif pro3<pro1 and pro3<pro2:
    print('Você deveria comprar o terceiro produto R$'.format(pro3))


    


