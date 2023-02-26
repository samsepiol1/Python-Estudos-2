import base64
from crypto.Cipher import aes

#criando uma chave de criptografia
chave = "0123456789ABCDEF"
aes = AES.new(chave, AES.MODE_ECB)

#recebe o arquivo a ser criptografado

arquivo = raw_input()

#ler o arquivo e corrigir o seu tamanho
#o tanho dever ser um multiplo de 16 caracters
arq_entrada = open(arquivo, "r")
arq_entrada = arq_entrada.read()

#caso o tamanho nao seja muliplo de 16 ele verifica quantos caracteres
#faltam para prencher e os preenche com o caractere '#'
cryptoSaida = arq_entrada+'#'*(16-len(arq_entrada)%16)

#criptografando o arquivo corrigido
#alem disso vamos colocar os dados criptografados
#em uma forma que caracteres estranhos nao aparecam
texto_cifrado = base64.b32encode(aes.encrypt(cryptoSaida))

#nesta etapa eh realizado os passos anteriores mas desta vez no titulo
titulo_novo=base64.b32encode(aes.encrypt(arquivo+'#'*(16-len(arquivo)%16)))

arq_saida = open(titulo_novo,'w')
arq_saida.write(texto_cifrado)
arq_saida.close()