salario_atual= float (input('Qual o seu Salario?R$:'))
if(salario_atual<=280):
    aumento=salario_atual*20/100
    salario_reajuste=salario_atual+aumento
    print('O salario antes do reajuste é de R${}\n o valor do auemnto foi de {}%\n o novo salario é igual a:R${}'.format(salario_atual,20,salario_reajuste))
elif(salario_atual>280) and(salario_atual<=700):
    aumento=salario_atual*15/100
    salario_reajuste=salario_atual+aumento
    print('O salario antes do reajuste é de R${}\n o valor do auemnto foi de {}%\n o novo salario é igual a:R${}'.format(salario_atual, 15, salario_reajuste))
elif(salario_atual>700)and(salario_atual<=1500):
    aumento=salario_atual*10/100
    salario_reajuste=salario_atual+aumento
    print('O salario antes do reajuste é de R${}\n o valor do auemnto foi de {}%\n o novo salario é igual a:R${}'.format(salario_atual,10,salario_reajuste))
elif(salario_atual>1500):
    aumento=salario_atual*5/100
    salario_reajuste=salario_atual+aumento
    print('O salario antes do reajuste é de R${}\n o valor do auemnto foi de {}%\n o novo salario é igual a:R${}'.format(salario_atual,5,salario_reajuste))






