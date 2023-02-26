estudantes = []
for i in range(4):
  estudantes.append(input("Digite o nome do aluno: "))

for x in estudantes:
  print("Aluno {}: {}".format(estudantes.index(x), x))
  list = ['primeiro', 'segundo', 'terceiro']
  print(', '.join(list))