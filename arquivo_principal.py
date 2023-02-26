from arquivoteste import horario
from onibus_troco import troco1
operecao=int(input('1-Saber Troco\n2-Ver Horario\n3-Sair'))
if operecao==1:
    troco1()
elif operecao==2:
    horario()
elif operecao==3:
    print('Saindo da aplicação...')
    exit()


