import time
def abre_arquivo():
    try:
     arquivo=open('arquivodidop.txt')
     return True
    except Exception as erro:
        print('Aconteceu algum erro', erro)
        return False
while not abre_arquivo():
    print('Tentando Abrir o arquivo')
    time.sleep(1)

print('O arquivo Abriu')






