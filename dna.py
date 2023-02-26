entrada = open("bacteria.fasta").read()
saida = open("bacteria.html","w")

cont = {}

for i in ['A','T','C','G']:
    for j in ['A','T','C','G']:
        cont[i+j] = 0


entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
    cont = [entrada[k]+entrada[k+1]]
i = 1
for k in cont:
    saida.write("<div></div>)


