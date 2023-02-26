num1=float(input('DIGITE UM NÚMERO AQUI:'))
num2=float(input('DIGITE OUTRO NÚMERO AQUI:'))
op=int(input('QUAL OPERAÇÃO DESEJA REALIZAR 1-SOMA\n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO:'))
resultado=0

if op==1:
    resultado=num1+num2
    print('{:.1f}'.format(resultado))
    if resultado>0:
        print('NUMERO POSITIVO')
    else:
        print('NUMERO NEGATIVO')

    if resultado%2==0:
        print('NUMERO PAR')
    else:
        print('NUMERO IMPAR')
    if resultado/1==resultado:
        print('NUMERO INTEIRO')
    else:
        print('NUMERO DECIMAL')

if op==2:
    resultado=num1-num2
    print('{:.1f}'.format(resultado))
    if resultado>0:
        print('NUMERO POSITIVO')

    else:
        print('NUMERO NEGATIVO')

    if resultado%2==0:
        print('NUMERO PAR')
    else:
        print('NUMERO IMPAR')
    if resultado/1==resultado:
        print('NUMERO INTEIRO')
    else:
        print('NUMERO NEGATIVO')

if op==3:

    resultado=num1*num2
    print('{:.1f}'.format(resultado))
    if resultado>0:
        print('NUMERO POSITIVO')

    else:
        print('NUMERO NEGATIVO')
    if resultado%2==0:
        print('NUMERO PAR')
    else:
        print('NUMERO IMPAR')
    if resultado/1==resultado:
        print('NUMERO INTEIRO')
    else:
        print('NUMERO DECIMAL')

if op==4:
    resultado=num1/num2
    print('{:.1f}'.format(resultado))
    if resultado>0:
        print('NUMERO POSITIVO')

    else:
        print('NUMERO NEGATIVO')
    if resultado%2==0:
        print('NUMERO PAR')
    else:
        print('NUMERO IMPAR')
    if resultado/1==resultado:
        print('NUMERO INTEIRO')
    else:
        print('NUMERO DECIMAL')







