n1=int(input('Insira aqui um numero:'))
i=1
t=0
while t<n1:
    t=i*(i+1)*(i+2)
    i+=1
if t==n1:
    print('{} é triangular'.format(n1))
else:
    print('{} não é triangular'.format(n1))

