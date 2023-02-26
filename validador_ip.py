def ip_ok(ip):
    ip=ip.split('.')
    for byte in ip:
        if int(byte)>255:
            return False
arq=open('ips.txt')
validos=open('validos.txt','w')
invalidos=open('invalidos.txt','w')
for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
        validos=open('validos.txt','rb')
    else:
        invalidos.write(linha)
        invalidos=open('invalidos.txt','rb')
ip_ok('192.168.101.1')
arq.close()
validos.close()
invalidos.close()