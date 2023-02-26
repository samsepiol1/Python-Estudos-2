cadastro=input('Insira aqui se o cliente é cadastrado ou não:C/N').upper()
litros=int(input('Quantos Litros ?'))
tipo_gasolina=input("G-Gasolina A-Alcool").upper()
total_sem_descontos_gas=litros*4.43
total_sem_descontos_al=litros*3.79
valor_com_desconto_gas=(total_sem_descontos_gas*2.5)/100
valor_com_desconto_al=(total_sem_descontos_al*2.5)/100
valor_com_desconto2=0
if(cadastro=='N') and(tipo_gasolina=='G'):
    print('O total a ser pago é igual a {}'.format(total_sem_descontos_gas))
elif(cadastro=='N') and(tipo_gasolina=='A'):
    print('O total a ser pago é igual a {}'.format(total_sem_descontos_al))
if(tipo_gasolina=='A') and (litros<=20):

    valor_com_desconto2=(valor_com_desconto_al*3.0)/100


    print("Parabèns, desconto de 3porcento:{:.2f}".format(valor_com_desconto2))
elif(tipo_gasolina=='A') and(litros>20):
    valor_com_desconto_al=(valor_com_desconto_al*5.0)/100

    print("Parabéns, desconto de 5porcento:{:.2f}".format(valor_com_desconto_al))
elif(tipo_gasolina=='G') and (litros<=20):
    valor_com_desconto_gas=(total_sem_descontos_gas*4.0)/100
    valor_final=valor_com_desconto_gas*litros
    print('Parabéns, desconto de 4porcento:{:.2f}'.format(total_sem_descontos_gas))
elif(tipo_gasolina=='G') and(litros>20):
    valor_com_desconto_gas(total_sem_descontos_gas*6.0)/100
    print('Parabéns, desconto de 6porcento:{:.2f}'.format(total_sem_descontos_gas))
