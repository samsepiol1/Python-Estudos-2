import hashlib
login_cript=hashlib.md5()
senha_cript=hashlib.md5()
login=input('Digte seu Login:')
senha=input('Digite aqui sua Senha:')
trans=str.encode(login)
trans2=str.encode(senha)
login_cript.update(trans)
senha_cript.update(trans2)
criptografado=login_cript.hexdigest()
criptografado2=senha_cript.hexdigest()
print(criptografado)
print(criptografado2)
arquivo=open('teses.txt','w')
arquivo.write(criptografado)
arquivo.write(criptografado2)
arquivo.close()
