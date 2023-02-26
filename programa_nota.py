nota1=float(input('INSIRA A PRIMEIRA NOTA:'))
nota2=float(input('INSIRA A SEGUNDA NOTA:'))
media=(nota1+nota2)/2
if media>=9 and media <=10:
    print('VOCÊ TIROU O CONCEITO A')
    print('Primeira nota {:.2f}'.format(nota1))
    print('Segunda nota {:.2f}'.format(nota2))
    print('Média obtida {:.1f}'.format(media))
    print('APROVADO!')
elif media>=7.5 and media <9:
    print('VOCÊ TIROU O CONCEITO B')
    print('Primeira nota {:.2f}'.format(nota1))
    print('Segunda nota {:.2f}'.format(nota2))
    print('Média obtida {:.1f}'.format(media))
    print('APROVADO!')
elif media>=6.0 and media<7.5:
    print('VOCÊ TIROU O CONCEITO C')
    print('Primeira nota {:.2f}'.format(nota1))
    print('Segunda nota {:.2f}'.format(nota2))
    print('Média obtida {:.1f}'.format(media))
    print('APROVADO!')
elif media>=4.0 and media<6.0:
    print('VOCÊ TIROU O CONCEITO D ')
    print('Primeira nota {:.2f}'.format(nota1))
    print('Segunda nota {:.2f}'.format(nota2))
    print('Média obtida {:.1f}'.format(media))
    print('REPROVADO!')
elif media<4.0:
    print('VOCÊ TIROU O CONCEITO E ')
    print('Primeira nota {:.2f}'.format(nota1))
    print('Segunda nota {:.2f}'.format(nota2))
    print('Média obtida {:.1f}'.format(media))
    print('REPROVADO!')



