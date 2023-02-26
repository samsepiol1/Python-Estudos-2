preco=float(input('Digitei o preço da mercadoria R$'))
descon=float(input('Digite o percentual de desconto %:'))
preco_atual=preco-((preco*descon)/100)
per_descon=preco-preco_atual
print('O novo preço com desconto é igual a: {}R$'.format(preco_atual))
print('O desconto feito no produto foi igual a:{}R$'.format(per_descon))














