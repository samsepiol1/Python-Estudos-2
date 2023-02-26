n1= int (input('Digite aqui um valor:'))
n2= int (input('Digite aqui outro valor:'))
oper=input('1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n:')
if(oper=='1'):
    s=n1+n2
    print(s)
if(oper=='2'):
    s=n1-n2
    print(s)
if(oper=='3'):
    s=n1*n2
    print(s)
if(oper=='4'):
 s=n1/n2
 print(s)
elif(s<0):
    print('numero negativo')
elif (s>0):
    print('numero positivo')
if(s%2==0):
    print('numero par')
else:
    print('numero impar')




