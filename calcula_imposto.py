def calcula_imposto(taxaImposto,custoItem):
    taxa_total=custoItem+(custoItem*(taxaImposto/100))
    return taxa_total
pergunta=input('Deseja executar o programa? S/N')
while pergunta=='S':
  print('='*30)
  print('{:^30}'.format('IMPÔSTOMETRO'))
  print('='*30)
  imposto=float(input('Qual o valor em % da taxa de impostos:'))
  item=float (input('Digite aqui o valor em R$ do Item a ser adquirido:'))
  print('O valor do produto antes da taxa de impostos era de:R${}'.format(item))
  print('O valor do produto após da taxa de impostos é de:R${}'.format(calcula_imposto(imposto,item)))












