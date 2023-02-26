import socket
import threading

ip='0.0.0.0'
porta=9999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,porta))
server.listen(5)
def cliente(cliente_socket):
    resposta=cliente_socket.recv(24)
    print('Resposta %s'% resposta)
    cliente_socket.send('Salve Pessoal')
    cliente_socket.close()
while True:
    client,addr=server.accept()
    print('Conexão Recebida por {} {}'.format(addr[0],addr[1]))
    cliente=threading.Thread(target=cliente,args=(client,))
    cliente.start()






