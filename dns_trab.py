from socket import getaddrinfo
import socket
import pprint
var=getaddrinfo(None,'smtp',0,socket.SOCK_STREAM,0)
trans=var[0]
trans2=trans[0:3]
print(trans2)
s=socket.socket(*trans2[0:3])
print(s)
'Ver a qual porta o protocolo smtp pode se associar'

'Lista se estar disponivel atraves da porta'
import socket
from socket import getaddrinfo
var=getaddrinfo(None,53,0,socket.SOCK_DGRAM,0,socket.AI_PASSIVE)
print(var)

