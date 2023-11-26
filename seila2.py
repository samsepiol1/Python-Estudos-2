import math
sair=0
while sair==0:
    num1=int(input('Digite um número:'))
    num2=int(input('Digite o segundo número:'))
    opcao= int(input('1-SOMA 2- SUB  3-DIV 4-MULT 5-EXPO 0-SAIR'))
    if opcao==1:
        resultado=num1+num2
        print(resultado)
    elif opcao==2:
        resultado=num1-num2
        print(resultado)
    elif opcao==3:
        resultado=num1/num2
        print(resultado)
    elif opcao==4:
        resultado=num1*num2
        print(resultado)
    elif opcao==5:
        math.exp(num1)
    elif opcao==0:
        print('DESLIGANDO....')
        exit()





