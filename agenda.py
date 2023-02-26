import time
import os
import sys
import string
import pymysql
from tela_u import opcaoUsuario

def conectaBanco():
    HOST="localhost"
    USER="root"
    passwd=""
    BANCO="Agenda"
    try:
        conecta=pymysql.connect(HOST,USER,passwd)
        conecta.select_db(BANCO)
    except NameError as e:
        print("Erro")
        menu=input()
        os.system("cls")
        opcaoUsuario()
    return conecta
def funcCadastrar(conecta):
    print("DIGITE OS DADOS")
    name=str(input("Nome:")).upper()
    address=str(input("Endereço:")).upper()
    fone=str(input("Telefone:")).upper()
    mail=str(input("Email:")).upper()
    cursor=conecta.cursor()
    sql = "INSERT INTO pessoas (nome,endereco,email,telefone) VALUES ('" + name + "','" + address + "','" + mail + "','" + fone + "')"
    try:
        cursor.execute(sql)
        conecta.commit()

    except SyntaxError as e:
        print("Erro: " + sql)
        print(e)
    print("DADOS GRAVADOS COM SUCESSO")
    conecta.close()
    menu=input()
    os.system("cls")
    opcaoUsuario()


def funcConsultar(conecta):
    name = str(input("\nDigite o Nome a Pesquisar: "))
    name = (name.upper())
    cursor = conecta.cursor()
    sql = "SELECT * FROM pessoas WHERE nome='" + name + "'"
    resultados = 0

    try:
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for dados in resultado:
          ide = dados[0]
          nome = dados[1]
          endereco = dados[2]
          email = dados[3]
          telefone = dados[4]
          resultados = int(resultados)
          resultados = resultados + 1
          print("\n----------------------------\n")
          print(" ID: %s\n Nome: %s\n Endereco: %s\n Email: %s\n Telefone: %s" % (ide, nome, endereco, email, telefone))
    except SyntaxError as e:
        print("Erro: " + sql)
        print(e)

    print("\n\nForam encontrados %d resultados" % resultados)
    conecta.close()
    menu = input()
    os.system("cls")
opcaoUsuario()


def funcalterar(conecta):
    print("Digite seus Dados:")
    ide=input("ID do novo contato:")
    novo_nome=input('Novo Nome:').upper()
    cursor=conecta.cursor()
    sql = "UPDATE pessoas SET nome='" + novo_nome + "' WHERE id='" + ide + "'"
    try:
        cursor.execute(sql)
        conecta.commit()
    except EOFError as e:
        print("Error")
        print(e)
    print("Alteração Feita com sucesso")
    conecta.close()
    menu=input()
    os.system("cls")
    opcaoUsuario()

def funcexcluir(conecta):
    print('Digite os Dados')
    ide_exclusao=input('Ide a Excluir:')
    sql = "DELETE FROM pessoas WHERE id='" + ide_exclusao + "'"
    cursor=conecta.cursor()
    try:
            cursor.execute(sql)
            conecta.commit()
            funcexcluir()

    except Exception as e:
        print("Error")
        print(e)

    print("Exclusão feita com sucesso")
    conecta.close()
    menu=input()
    os.system("cls")
    opcaoUsuario()
def funcmostrartodos(conecta):
    resultados=0
    cursor=conecta.cursor()
    sql = "SELECT * FROM pessoas;"
    try:
     cursor.execute(sql)
     resultado=cursor.fetchall()
     for dados in resultado:
         ide = dados[0]
         nome = dados[1]
     endereco = dados[2]
     email = dados[3]
     telefone = dados[4]
     resultados = int(resultados)
     resultados = resultados + 1
     print('---------------------')
     print(nome,endereco,email,telefone)
    except Exception as e:
        print("ERRO")
        print(e)
    print(resultados)
    conecta.close()
    menu=input()
    os.system("cls")
    opcaoUsuario()

























