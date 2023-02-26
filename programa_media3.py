nota1=float(input('DIGITE A PRIMEIRA NOTA:'))
nota2=float(input('DIGITE A SEGUNDA NOTA:'))
nota3=float(input('DIGITE A TERCEIRA NOTA:'))
media=(nota1+nota2+nota3)/3
if media<10 and media>=7:
    print('APROVADO!!!')
elif media<7:
    print('REPROVADO')
elif media==10:
    print('APROVADO COM DISTINÇÃO')






