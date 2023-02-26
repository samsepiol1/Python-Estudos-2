import sys
import os
import platform



argumentos=sys.argv #arg1 método arg2 n1 arg3 n2

def soma(n1,n2):
    retornar=n1+n2
    return retornar
def sub (n1,n2):
    retornar=n1-n2
    return retornar
def mult(n1,n2):
    retornar=n1*n2
    return retornar
def div(n1,n2):
 retornar=n1/n2
 return retornar



if argumentos[1]=="soma":
    resp=soma(float(argumentos[2]),float(argumentos[3]))
    print(resp)
    print("O nome do seu Sistema Operacional É: {}".format(platform.platform()))
    print("Você está usando a versão {}".format((platform.release())))
    print("Você está usando um Windows{}".format(os.name.upper()))










elif argumentos[1]=="sub":
    resp=sub(float(argumentos[2]),float(argumentos[3]))
    print(resp)
elif argumentos[1]=="mult":
    resp=mult(float(argumentos[2]), float (argumentos[3]))
    print(resp)
elif argumentos[1]=="div":
    resp=div( float (argumentos[2]),float(argumentos [3]))
    print(resp)
elif argumentos[1]=="help":
    print('Lista de operações\nsoma n1 n2(soma os numeros n1 e n2)\nsub n1 n2(subtrai os numeros n1 e n2) \nmult n1 n2 (multiplica os numeros n1 e n2) \ndiv n1 n2(divide n1 e n2)')

else:
    print("Operação inexistente")









