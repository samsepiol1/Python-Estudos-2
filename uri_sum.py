from math import sqrt
linha = input().split()
x1 = float(linha[0])
y1 = float(linha[1])
linha2 = input().split()
x2 = float(linha2[0])
y2 = float(linha2[1])

distancia = sqrt( (x2-x1)**2 + (y2-y1)**2 )

print('{:.4f}'.format(distancia))


