from math import sqrt,pow
a=int(input('INFORME O VALOR DE A:'))
if a==0:
    print('A equação não é de segundo grau')
else:
    b=int(input('INFORME O VALOR DE B:'))
    c=int(input('INFORME O VALOR DE C:'))
    delta=pow(b,2)-4*a*c

if delta<0:
    print('A equação  não possui raizes reais')
elif delta==0:
    x1 = (b + sqrt(delta)) / 2 * a
    print('A equação possui uma raiz real!')
    print('Raiz={}'.format(x1))

elif delta>0:
    x1 = (b + sqrt(delta)) / 2 * a
    x2=(b-sqrt(delta))/2*a
    print('A equação possui duas raizes reais!')
    print('A primeira raiz é igual a {}'.format(x1))
    print('A segunda raiz é igual a {}'.format(x2))
    



















