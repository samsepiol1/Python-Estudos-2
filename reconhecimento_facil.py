texto=open('mensagem.txt')
saida=open('cripto.txt','w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'abcdefghijklmnopqrstuvxwyz'.lower():
            saida.write('*')
        else:
            saida.write(letra)
texto.close()



