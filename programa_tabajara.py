salario=float(input('INFORME AQUI O SEU SALÁRIO:'))
aum=(10/100+1)*salario
valor_aumento=0
if salario<=280:
    aum=(20/100+1)*salario
    valor_aumento=aum-salario
    print('Salario antes do reajuste:{}R$'.format(salario))
    print('Percentual aplicado de 20%')
    print('O valor atribuido foi de {}'.format(valor_aumento))
    print('O seu novo salário é de R${:.1f}'.format(aum))
elif salario>280 and salario<=700:
    aum=(15/100+1)*salario
    valor_aumento=aum-salario
    print('Salario antes do reajuste:{}'.format(salario))
    print('Percentual aplicado de 15%')
    print('O valor atribuido foi de:{:.1f}'.format(valor_aumento))
    print('O seu novo salário é de R${:.1f}'.format(aum))
elif salario>700 and salario <=1500:
    valor_aumento=aum-salario
    print('Salario antes do reajuste {}'.format(salario))
    print('O percentual aplicado foi de 10%')
    print('O valor atribuido foi de {:.1f}'.format(valor_aumento))
    print('O seu novo salário é de R${:.1f}'.format(aum))
elif salario>1500:
    aum=(5/100+1)*salario
    valor_aumento=aum-salario
    print('Salario antes do reajuste {}'.format(salario))
    print('Percentual aplicado 5%')
    print('O valor atribuido foi de R${:.1f}'.format(valor_aumento))
    print('O seu novo salário é de R${:.1f}'.format(aum))









