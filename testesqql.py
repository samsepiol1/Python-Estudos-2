import pymysql
conexao=pymysql.connect(host='localhost',user='root',passwd='',db='cursox')
cursor=conexao.cursor()
teste=cursor.execute("SHOW DATABASES")
print('Quantidade de tabelas:{}'.format(teste))
for x in cursor:
    print("NOMES DAS TABELA:")
    print(x)



