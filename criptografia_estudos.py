import change
def trocador(InputStr,InputStr2):
    resultado=InputStr
    if InputStr==InputStr2:
        print('Troca não vai ser possível')
    elif InputStr!=InputStr2:
        resultado=InputStr2
        return resultado





texto=open('mensagem.txt','r')
saida=open('cripto.txt','w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'abcdefghijklmnopqrstuvxwyz'.lower():
            saida.write(letra.replace(letra,"*"))
        else:
            saida.write(letra)
    login=open('cripto.txt','r')
    texto.read()

