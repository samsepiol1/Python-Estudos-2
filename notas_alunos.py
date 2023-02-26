nota1=float(input('Digite aqui a sua primeira nota'))
nota2=float(input('Digite aqui a sua segunda nota'))
media=(nota1+nota2)/2
if nota1 and nota2 >10:
    print('NOTA INVÁLIDA')
elif media==10:
    print('APROVADO COM DISTINÇÃO!')
elif media>=7:
    print('APROVADO!')
elif media<7:
    print('REPROVADO!')











