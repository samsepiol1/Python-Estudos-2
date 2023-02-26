import argparse,random,sys,socket
MAX_BYTES=65535
def server(interface,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((interface,port))
    print('Escutando at',sock.getsockname())

