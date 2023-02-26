numero_cigarros=int  (input("Quantos cigarros você fuma por dia ? "))
numero_dia=int (input("a quantos anos ele fumou:"))
totalcigarro=(numero_dia*365)*numero_cigarros
dias_perdido=(totalcigarro*10)/24
print('Dias perdido {:.1f}'.format(dias_perdido))




