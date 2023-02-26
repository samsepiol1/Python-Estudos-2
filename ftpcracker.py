import socket
import re
import sys
def connection (ip,user,passw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Trying ' + ip + ':' + user + ':' + passw)

    sock.connect(('ip',21))

    data = sock.recv(1024)

    sock.send('USER' + user +'\r\n')

    data = sock.recv(1024)

    sock.send('Password'+passw + '\r\n')

    data = sock.recv(1024)

    sock.close()
    return  data

user = 'User'
password = ['pass1','pass2']

for password in password:
    print(connection('ip',user,password))

