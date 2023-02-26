import os
import time
import sys
import pymysql
import agenda

def opcaoUsuario():
    os.system("clear")
    print(
    "===================================")
    print
    ("======= Agenda de Contatos ========")
    print
    ("===================================")
    opcao=int (input('Escolha a opcao desejada\n\n[1] - Cadastrar\n[2] - Consultar\n[3] - Alterar\n[4] - Excluir\n[5] - Mostrar Todos\n[6] - Sair'))
    try:

        if opcao < 1 or opcao > 6:
            os.system("cls")
            print
            "OPCAO INVALIDA: Verifique o valor digitado"
            time.sleep(2)
            opcaoUsuario()
    except:
        os.system("cls");
        print
        "OPCAO INVALIDA: Verifique o valor digitado"
        time.sleep(2)
        opcaoUsuario()

    if opcao == 1:
        conecta = agenda.conectaBanco()
        agenda.funcCadastrar(conecta)

    elif opcao == 2:
        conecta = agenda.conectaBanco()
        agenda.funcConsultar(conecta)

    elif opcao == 3:
        conecta = agenda.conectaBanco()
        agenda.funcalterar(conecta)

    elif opcao == 4:
        conecta = agenda.conectaBanco()
        agenda.funcExcluir(conecta)

    elif opcao == 5:
        conecta = agenda.conectaBanco()
        agenda.funcMostrarTodos(conecta)

    elif opcao == 6:
        sys.exit()