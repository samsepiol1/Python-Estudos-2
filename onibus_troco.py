import time
import PyPDF2
def calcula_troco(dinheiro,valor_pago):
    troco=dinheiro-valor_pago
    return troco
def troco1():
 controle=True
 valor_pago1=0
 while controle==True:
  linha=input('Insira a letra do ônibus aqui:').upper()
  dinheiro1=float(input('Insira a quantidade em dinheiro fornecida:'))
  if linha=='A':
    valor_pago1=4.45
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Continuar a rodar? S/N').upper()
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='B':
    valor_pago1=4.45
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Cotinuar a rodar? S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='C':
    valor_pago1=3.85
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja continuar a rodar S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='G':
    valor_pago1=4.45
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Continuar a rodar? S/N')
    if rodar=='N':
        print('Fechando Aplicação')
        exit()
  elif linha=='H':
    valor_pago1=3.25
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Continuar a rodar? S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='J':
    valor_pago1=4.45
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Continuar a rodar? S/N')
    if rodar=='N':
        print('Fechando Aplicação')
        exit()
  elif linha=='L':
    valor_pago1=3.85
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Desejar Continuar a rodar S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='M':
    valor_pago1=4.45
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja continuar a rodar S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='N':
    valor_pago1=1.95
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Continuar a rodar S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()
  elif linha=='P':
    valor_pago=4.45
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja Continuar a rodar? S/N')
    if rodar=='N':
        print('Fechando aplicação...')
        exit()
  elif linha=='V':
    valor_pago1=3.85
    resultado_troco=calcula_troco(dinheiro1,valor_pago1)
    print('Troco:{}'.format(resultado_troco))
    rodar=input('Deseja continuar a rodar? S/N')
    if rodar=='N':
        print('Fechando Aplicação...')
        exit()





