import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server='pythonprogramming.net'
def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False
for x in range(1,26):
    if pscan(x):
        print  ('Port',x,'Is Open')
    else:
        print('Port',x,'\033[1;31mIs Closed')