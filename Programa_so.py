import os
import platform
import sys
argumentos=sys.argv

if argumentos[1]=="1":
    print(platform.platform())
elif argumentos[1]=="2":
    print(os.name.upper())
elif argumentos[1]=="3":
    print(platform.release())
elif argumentos[1]=="help":
    print('=' * 30)
    print('{:30}'.format('Programa Sistema Operacional'))
    print('=' * 30)
    print('1-Saber Nome do Sistema')
    print('2-Saber Família do Sistema')
    print('3-Saber Versão do Sistema')
    print('=' * 30)
elif argumentos[1]=="":
    print("Digite o comando Help para mais informações")
else:
    print('Operação inválida')






