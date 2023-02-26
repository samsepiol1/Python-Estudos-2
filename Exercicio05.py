parede_metros= float((input('Digite aqui o tamanho da parede em metros')))

parede_litros=parede_metros/3
preco_tinta=80
latas=18
quantidade_latas=parede_litros/latas
total_preco=quantidade_latas*preco_tinta
print('Você gastara R${:.2f} com {:.2f} latas de tinta'.format(total_preco,quantidade_latas))



