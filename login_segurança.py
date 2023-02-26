def trocador(InputStr,InputStr2):
    resultado=InputStr
    if InputStr==InputStr2:
        print('Troca não vai ser possível!')
    elif InputStr!=InputStr2:
        resultado=InputStr2
        return resultado
login=input('Login:')
texto=open('mensagem.txt','rb')
saida=open('cripto.txt','w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'abcdefghijklmnopqrstuvxwyz'.lower():
            saida.write(letra.replace(letra,"*"))
        else:
            saida.write(letra)


