valor_hora=float (input('Informe o quanto você ganha por hora:'))
quantidade_trabs=float (input('Quantidade de horas trabalhada trabalhada'))
salario_bruto=valor_hora*quantidade_trabs
desconto_FGTS=salario_bruto*11/100
desconto_INSS=salario_bruto*10/100
desconto_IR=salario_bruto*5/100
total_desconto=desconto_IR+desconto_INSS
salario_liquido=salario_bruto-desconto_INSS-desconto_IR
if(salario_bruto<=900):
    print('IR:Isento\nINSS:R${}\nFGTS R$:{}\nTotal de Descontos:R${}\nSalario Liquido=R${}'.format(desconto_INSS,desconto_FGTS,desconto_INSS,salario_liquido))

elif(salario_bruto>900) and (salario_bruto<=1500):
    print('IR:R${}\nINSS:R${}\nFGTS:R${}\nTotal de Descontos:R${}\nSalario Liquido=R${}'.format(desconto_IR,desconto_INSS,desconto_FGTS,total_desconto,salario_liquido))
elif(salario_bruto<=2500):
 desconto_IR=salario_bruto*10/100
 total_desconto=desconto_IR+desconto_INSS
 print('IR:R${}\nINSS:R${}\nFGTS:R${}\nTotal de Descontos:R${}\nSalario Liquido=R${}'.format(desconto_IR,desconto_INSS,desconto_FGTS,total_desconto,salario_liquido))
elif(salario_bruto>1500):
 desconto_IR=salario_bruto*20/100
 total_desconto=desconto_IR+desconto_INSS
 print('IR:R${}\nINSS:R${}\nFGTS:R${}\nTotal de Descontos:R${}\nSalario Liquido=R${}'.format(desconto_IR,desconto_INSS,desconto_FGTS,total_desconto,salario_liquido))












