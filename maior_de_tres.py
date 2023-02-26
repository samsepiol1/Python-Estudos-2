num1=float(input('Digite um número aqui:'))
num2=float(input('Digite um segundo número aqui:'))
num3=float(input('Digite um terceiro número aqui'))
if num3>num1 and num3>num2:
    print('O Terceiro número é o maior')
elif num2>num1 and num2>num3:
    print('O segundo número é o maior')
elif num1>num2 and num1>num3:
    print('o primeiro número é o maior')

if num3<num1 and num3<num2:
    print('O número três é o menor')
elif num2<num1 and num2<num1:
    print('o número dois é menor')
elif num1<num2 and num1<num3:
    print('o primeiro número é o menor')
else:
    print('Os números digitados são iguais')



