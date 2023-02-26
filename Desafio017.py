'''from math import pow, sqrt
cat1=float (input('Coloque aqui o valor do cateto oposto:'))
cat2=float (input('Coloque aqui o valor do cateto adjacente:'))
hip=pow(cat1,2)+ pow(cat2,2)
print('O VALOR DA HIPOTENUSA É IGUAL A {:.2f}'.format(sqrt(hip)))'''
from math import hypot
cat1=float (input('Coloque aqui o valor do cateto oposto:'))
cat2=float (input('Coloque aqui o valor do cateto adjacente:'))
hip=hypot(cat1,cat2)
print('O resultado da hipotenusa é igual a: {:.2f}'.format(hip))









