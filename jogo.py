palavra=input("Digite a palvra secreta:").lower().strip()
for x in range(100):
    print()
digitadas=[]
acertos=[]
erros=0
while True:
    senha=""
    for letra in palavra:
        senha+=letra if letra in acertos else "."
    print(senha)
    if senha==palavra:
        print("Você acertou")
        break
    tentativa=input("Digite uma letra:").lower().strip()
    if tentativa in digitadas