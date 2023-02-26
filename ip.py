import socket
hostname='www.python.org'
endereco=socket.gethostbyname_ex(hostname)
print('O ENDREÇO DE IP DO {} É {}'.format(hostname,endereco))