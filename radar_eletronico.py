velocidade_corredor=int(input('Digite a Velocidade do motorista:'))
print('km/h:{}'.format(velocidade_corredor))
if velocidade_corredor>=80:
    print('Execedeu o limite de velocidade')
    multa=velocidade_corredor*7
    print('O valor da multa é de:R${}'.format(multa))
