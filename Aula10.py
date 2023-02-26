import string
arquivo=open('arquivo.txt','r+')
a=list(string.ascii_lowercase)
b=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
letra='Lucas'
letra.split()
if letra[3]=="a":
    print('Criptografia Baseada no Algoritmo de César:')
    print(a)
    print(b)

else:
    print('Não existe letra a no arquivo')

print('Arquivo Criptografado:')
arquivo.write('Lucas')


























