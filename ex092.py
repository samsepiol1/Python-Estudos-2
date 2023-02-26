nome=input('Insira aqui o seu nome:')
Quantidade_Salario='Salario'
ano_contrataco='Admissão'
ano_nascimento=int(input('Insira Aqui o Seu ano de nascimento:'))
ctps=input('Insira o número da sua carteira de trabalho:')
idade=2019-ano_nascimento
dicionario_dados={'Nome':nome,'Nascimento':ano_nascimento,'Carteira':ctps}
print(dicionario_dados)
if ctps!=0:
    salario=input('Digite aqui o seu salario:')
    ano_de_contratacao=input('Digite o ano de contratação:')
    dicionario_dados[Quantidade_Salario]=salario
    dicionario_dados[ano_contrataco]=ano_de_contratacao
    print(dicionario_dados)
    if idade>70:
        print('Já pode se aposentar!')

