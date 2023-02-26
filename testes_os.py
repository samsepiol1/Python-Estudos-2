
import socket
resultado=(socket.gethostbyname_ex('Deus'))
n=input('Deseja Obter informações da Placa de Rede: S/N')
if n=='S':
    print('Seu endereço ip é: {}'.format(resultado[2][1]))
else:
    print('Programa Encerrado')