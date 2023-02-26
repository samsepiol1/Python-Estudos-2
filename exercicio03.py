km_rodado=float(input('Quantos Quilometros você vai rodar com o carro?'))
dias=int(input('Por quantos dias você pretende ficar com o carro'))
preco_km=km_rodado*0.50
preco_dia=dias*100
preco_total=preco_km+preco_dia
print('O preço total do Aluguel foi de: {}R$'.format(preco_total))



