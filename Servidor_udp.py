import argparse, socket
from datetime import datetime

max_bytes=65535
def server(port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind('127.0.0.1',port)
    print('Escutando a porta at {}'.format(sock.getsockname()))
    while True:
     data,address=sock.recvfrom(max_bytes)
     text=data.decode('ascii')
     print('O cliente de {} fala {!r}'.format(address,text))
     text='Seu dado é {} bytes long'.format(len(data))
     data=text.encode('ascii')
     sock.send(data,address)
def client(port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text='O tempo é {}'.format(datetime.now())
    data=text.encode('ascii')
    sock.sendto(data,('127.0.0.1',port))
    print('O Sistema Operacional me deu {}'.format(sock.getsockname()))
    data,address=sock.recv(max_bytes) #danger!
    text=data.encode('ascii')
    print('O servidor {} respondeu {!r}'.format(address,text))
if __name__=='__main__':
 choices={'cliente':client,'Servidor':server}
 parser=argparse.ArgumentParser(description='Envie e Recceba um UDP local')
 parser.add_argument('role',choices=choices,help='Wich Role to Play')
 parser.add_argument('-p',metavar='PORT',type=int,default=1060,help='PORTA UDP(default 1060)')
 args=parser.parse_args()
 function(args.p)
 print(server(1060))


