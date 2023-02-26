import sys
import socket
import getopt
import threading
import subprocess

#definir variáveis globais
listen=False
command=False
upload=False
execute=''
target=''
upload_destination=''
port=0

def usage():
    print('Ferramenta de Rede')
    print()
    print("Usage: bhnet.py -t target_host -p")
    print("-l --listen - listen on [host]:[port] for")
    print()
    print("-e --execute==file_to_run")
    print('-c --command')
    print('- u --upload==destination')
    print()
    print()
    print("Exemples")
    print("bhnet.py -t 192.168.0.1 -p 5555 -1 -c")
    print("bhnet.py -t 192.168.0.1 -p 5555 -1 -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)

def client_sender(buffer):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((target, port))
            if len(buffer):
                client.send(buffer)
            while True:
             recv_len = 1
             response = ""
             while recv_len:
                 data = client.recv(4096)
             recv_len = len(data)
             response += data
             if recv_len < 4096:
                 break
            print(response)
            buffer = input("")
            buffer += "\n"
            client.send(buffer)

        except Exception as e:
            print(e)

        client.close()
def server_loop():
    global target
    if not len(target):
        target="0.0.0.0"
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(target,port)
    server.listen(5)
    while True:
          client_socket=server.accept()
          addr=server.accept()
          client_thread=threading.Thread(target=client_handler())
          client_thread=threading.Thread(args=(client_socket))

def run_command(command):
    command=command.rstrip()
    try:
        output=subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output = "Failed to execute command.\r\n"
    return output
def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):
        file_buffer=''
    while True:
            data=client_socket.recv(1024)
            if not data:
                   break
            else:
                     file_buffer+=data
    try:
     file_descriptor = open(upload_destination, "wb")
     file_descriptor.write(file_buffer)
     file_descriptor.close()
     client_socket.send("Successfully saved file to ¬% s\r\n" % upload_destination)
    except:
        client_socket.send("Failed to save file to %s\r\n" % -upload_destination)
        while True:
         client_socket.send("<BHP:#> ")

















def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
if not len(sys.argv[:1]):
    usage()



# lendo os comandos disponiveis nas opções
try:
    opts,args=getopt.getopt(sys.argv[1],"hle:t:p:cu",["help,listen,execute,target,port,comand,upload"])
except getopt.GetoptError as err:
    print (str(err))
    usage()
for o,a in opts:
    if o in ("-h","--help"):
        usage()
    elif o in("-l","--listen"):
        listen==True
    elif o in ("e","--excute"):
        execute=a
    elif o in ("c","--comandshell"):
        command==True
    elif o in("u","--upload"):
        upload_destination=a
    elif o in("-t","--target"):
        target=a
    elif o in("p","--port"):
        port=int(a)
    else:
        assert False,"Unhandled Option"
buffer=sys.stdin.read
client_sender(buffer)
if listen:
    server_loop()
main()







