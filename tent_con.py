import pymysql
def criar_conexao(host,user,passwd,db):
    conn2=pymysql.connect(host=host,user=user,passwd=passwd,db=db)
    return conn2
nome_db=input('Digite o nome do banco de dados')
conn=criar_conexao('localhost','root','',nome_db)
cursor=conn.cursor()
teste=cursor.execute("SHOW TABLES")
for x in cursor:
    print(x[0])




