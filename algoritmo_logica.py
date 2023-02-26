soma = 0

quantidade = 1

while quantidade<=8:
    nota = float(input("Nota"+str(quantidade)+":"))
    soma = soma+nota
    quantidade = quantidade+1
    media = soma/8
print("Media da turma=",media)
