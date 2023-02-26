#Bibliotecas usadas
import pymysql
import string
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
#Iniciar o WebScrap
sauce=urllib.request.urlopen('https://www.tecmundo.com.br').read()
soup=bs.BeautifulSoup(sauce,'lxml')
#Coleta de titulos das noticias
for coletas in soup.find_all('a',class_='nzn-main-item'):
    var_noticias=[coletas][0]['title']

#Coleta das noticias
driver=webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
driver.get('https://www.tecmundo.com.br/mercado/142333-5g-huawei-nao-banida-brasil-diz-mourao.htm')
html=driver.page_source
soup=bs.BeautifulSoup(html,'lxml')
for teses in soup.find_all('p'):
    nav=soup.p
    print(teses.text)
#Criar conexão com um Banco de Dados Local
def criar_conexao(host,user,passwd,db):
    conn2=pymysql.connect(host=host,user=user,passwd=passwd,db=db)
    return conn2
#Construir esse automatizador para não ter que abrir o MysqlWorkBench toda hora e digitar vários insert into
print ("===================================")
print("======= AUTOMYSQL ========")
print ("===================================")
nome_db=input('Digite o nome do banco de dados:')
opcao=input('1-Mostrar Tabelas\n2-Consultar Tabelas\n3-Deletar Dados\n4-Inserir dados')
conn=criar_conexao('localhost','root','',nome_db)
cursor=conn.cursor()
if opcao=='1':
    teste=cursor.execute('SHOW TABLES')
    print("Quantidade de tabelas:{}".format(teste))
    for x in cursor:
        print("Nome da Tabela: {}".format(x[0]))
elif opcao=='2':
    print('Estabelça as condições:')
    nome_atributo = input('Digite o atributo a ser selecionado:')
    nome_tabela= input('Digite o nome da tabela')
    nome_atri=input('Digite a condição where:')
    valor=input('digite a condição do valor:')
    teste=cursor.execute("SELECT {} FROM {} WHERE {} = '{}'".format(nome_atributo,nome_tabela,nome_atri,valor))
    print('Quantidade de resultado: {}'.format(teste))
    for x in cursor:
        print(x[0])
elif opcao=='3':
    del_tab=input('De qual tabela você quer deletar:')
    condicao=input('Coloque aqui o where')
    dado=input('Qual dado você quer apagar?')
    cursor.execute("DELETE FROM {} WHERE {} = '{}'".format(del_tab,condicao,dado))
    conn.commit()
    resultado_query=cursor.execute("DESC ALUNOS")
    for x in cursor:
        print(x)
    conn.close()
#Inserindo titulos no banco de dados
elif opcao=='4':
    valor='Mi Band 4 já está em pré-venda; entrega no Brasil para julho'
    cursor.execute("INSERT INTO noticias2(titulo) VALUES ('Xiaomi Mi Band 4 terá tela colorida');")
    conn.commit()









