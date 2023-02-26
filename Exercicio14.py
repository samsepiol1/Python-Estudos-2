ano=int(input('Digite um ano aqui:'))
if(ano%4==0) and (ano%100!=0) or ano(ano%400==0):
    print('o ano{} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
    
