from optparse import OptionParser  # opções em linha de comando.
from socket import *  # Sockets


def h2ip(host):
    """Pega um nome de host e devolve o IP"""
    try:
        ip = gethostbyname(host)
        return ip
    except:
        return None


def connecto(host, port):
    """Cria a conexão socket"""
    try:
        s = socket(AF_INET, SOCK_STREAM)  # TCP Socket
        s.connect((host, port))
        return s
    except:
        s.close()
        return None


def bgrabber(sock):
    """Faz o 'handshake' da conexão e retorna o banner do serviço daquela porta"""
    try:
        sock.send("Scann ...\r\n")
        banner = sock.recv(1024)
        return banner
    except:
        return None


def scan(host, port):
    """Começa a varredura de portas"""
    sock = connecto(host, port)
    setdefaulttimeout(5)  # default timeout 5 segundos
    if sock:
        print("[+] Conectado com %s:%d" % (host, port))
        banner = bgrabber(sock)
        if banner:
            print("[+] Banner: %s" % banner)
        else:
            print("[!] Não foi possivel returnar o banner do alvo")
            sock.close()  # Done
    else:
        print("[!] Não foi possivel conectar com %s:%d" % (host, port))


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-a", "--alvo", dest="host", type="string",
                      help="Insira o nome do host alvo", metavar="exemplo.com")
    parser.add_option("-p", "--porta", dest="portas", type="string",
                      help="Portas que deseja scanear separadas por virgulas", metavar="PORT")

    (options, args) = parser.parse_args()

    if options.host == None or options.ports == None:
        parser.print_help()
    else:
        host = options.host
        ports = (options.ports).split(",")
        try:
            ports = list(filter(int, ports))  # Armazena as portas numa lista.
            ip = h2ip(host)  # Nome do Domínio IP.
            if ip:
                print("[+] Executando Scanner: %s" % host)
                print("[+] Alvo IP: %s" % ip)
                for port in ports:
                    scan(host, int(port))
            else:
                print("[!] Host Inválido !!")
        except:
            print("[!] Lista de portas inválidas (ex: -p 21,22,53,..)")
