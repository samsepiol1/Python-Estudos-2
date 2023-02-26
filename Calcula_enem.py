def calcula_enem(linguagens,humanas,natureza,matematica,redacao):
    resultado1=linguagens+humanas+natureza+matematica+redacao
    resultado2=resultado1/5
    return resultado2
c='S'
while c=='S':
 print('='*30)
 print('{:30}'.format('CALCULADORA ENEM'))
 print('='*30)
 nota_lingua=float(input('DIGITE AQUI SUA NA EM LINGUAGENS:'))
 nota_humanas=float(input('DIGITE AQUI SUA NOTA EM HUMANAS:'))
 nota_natureza=float(input('DIGITE AQUI SUA NOTA EM NATUREZA:'))
 nota_matematica=float(input('DIGITE AQUI SUA NOTA EM MATEMATICA:'))
 nota_redacao=float(input('DIGITE AQUI SUA NOTA DA REDAÇÃO:'))
 media_final=calcula_enem(nota_lingua,nota_humanas,nota_natureza,nota_matematica,nota_redacao)
 if nota_lingua<450:
     print('Nota insuficiente em Linguagens')
 elif nota_humanas<450:
  print('Nota insuficiente em Humanas')
 elif nota_natureza<450:
  print('Nota insuficiente em Natureza')
 elif nota_matematica<450:
  print('Nota insuficiente em matematica')
 elif nota_redacao==0:
  print('Redação zerada')
 else:
  print('Sua média final foi de:{}'.format(media_final))
 c=input('DESEJA CONTINUAR A RODAR O PROGRAMA S/N')


