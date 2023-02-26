import os.path

arquivo=input('Insira o nome do arquivo aqui')
if os.path.isdir(arquivo):
    print('Já existe um arquivo com esse nome')
else:
    os.mkdir(arquivo)
    print('Arquivo criado com sucesso!')