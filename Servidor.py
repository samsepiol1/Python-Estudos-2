import socket
import threading

bind_ip="0.0.0.0"
bind_port=9999
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((bind_ip,bind_port))
servidor.listen(5)
print("Conectando{}{}".format(bind_ip,bind_port))
def handle_client(cliente_socket):
    request=cliente_socket.recv(1024)
    print('Recebendo{}'.format(request))
    cliente_socket.send("ACK!")
    cliente_socket.close()
while True:
    client,addr=servidor.accept()
    print("Aceitando conexões{}{}".format(addr[0],addr[1]))

    client_handler=threading.Thread(target=handle_client,args=(client,))
    client_handler.start()


