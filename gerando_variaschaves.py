"""from cryptography.fernet import Fernet
chave = Fernet.generate_key()
mensagem = "Minha mensagem ".encode()

f=Fernet(chave)
encrypted = f.encrypt(mensagem)


print(criptografar)"""

from cryptography.fernet import Fernet


def criptografar(mensagem):
    chave = Fernet.generate_key()
    dado = mensagem.encode()
    dado_letra = str(dado)
    f=Fernet(chave)
    encrypted=f.encrypt(dado)
    criptografar = f.decrypt(encrypted)
    print('chave embaralhada:',encrypted[::-1])
    print('chave real',encrypted)

criptografar('Lucas')


















