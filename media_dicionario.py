nome=input('Digite seu nome aqui:')
media=float(input('Digite sua média aqui:'))
if media>=6.0:
    print('Aluno Aprovado!')
    dicionario_media_nome = {nome: media}
    print("-------Média dos Alunos--------")
    print(f'a média de {nome} foi {media}')
else:
    print('Aluno Reprovado')
    dicionario_media_nome={nome:media}
    print(f'a média de {nome} foi {media}')


