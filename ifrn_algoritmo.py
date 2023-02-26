aluno = input('Digite aqui o seu nome:')
notas = []
quantidade = 1
status =''
while quantidade <=4:
    nota = int(input('Digite a nota:'))
    quantidade = quantidade + 1
    while nota>=0 and nota<=100:
        notas.append(nota)
        break
media = (notas[0] * 2 + notas[1] * 2 + notas[2] * 3 + notas[3]*3) / 10
if media>=60:
    status = 'Aprovado'
elif media >=30 and media<60:
    status = 'Em recuperação'
elif media<30:
    status = 'Reprovado'
print("O Aluno: {} obteve a média {} e está {}".format(aluno,media,status))









