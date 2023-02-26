from cryptography.fernet import  Fernet

chave = Fernet.generate_key()

def criar_arquivo():

    file = open('chave.key', 'wb')
    file.write(chave)
    print('Chave Gerada:',chave)
    file.close()
def ler_arquivo():
    file= open('chave.key','rb')
    chave_lida = file.read()
    print('chave lida',chave_lida)
    file.close()

criar_arquivo()
ler_arquivo()




