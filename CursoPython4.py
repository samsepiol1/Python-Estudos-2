n1=input('Digite o primeiro numero ')
n2=input('digite o segundo numero')
n3=input('digite um terceiro numero')
menor=n1
maior=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n2 and n3<n2:
    menor=n3
    #analisando o menor número
print('O menor número é o número {}'.format(menor))

if n2>n1 and n2>n3:
    maior=n2
if n3>n2 and n3>n1:
    maior=n3
print('o maior número é igual a {}'.format(maior))





