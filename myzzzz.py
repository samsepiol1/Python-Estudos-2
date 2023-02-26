import pymysql
connection = pymysql.connect(host='localhost',user='root',password='',db='cursox',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
nome=input('Digite o endereço que quer inserir no DB')
tabela=input('Digite um nome de uma tabela')
atributo=input('Digite um atributo:')


try:
    with connection.cursor() as cursor:
        sql="INSERT INTO `alunos` (`aluno_nome`, `aluno_endereco`) VALUES (%s, %s)"
        cursor.execute(sql, ('Ducas','Parnamirim'))
        for c in range(2):
            sql2 = "INSERT INTO `alunos`(`aluno_nome`), ` VALUES(%s))"
            cursor.execute(sql2, (nome))
            connection.commit()

        connection.commit()
finally:
    connection.close()

controle=connection.cursor()



