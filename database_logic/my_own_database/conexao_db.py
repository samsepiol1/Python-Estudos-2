import sqlite3
from database_logic.my_own_database import dados



conn = sqlite3.connect('users.db')

c = conn.cursor()

usuarios = dados.leitura_arquivo()

#c.execute("""CREATE TABLE instagram_users (users) """"")

#Inserir No banco de dados
def insert_emp(users):
    with conn:
        c.execute("INSERT INTO instagram_users VALUES (:users)", {'users':users})

#Pegar dados
def get_emps_by_name():
    c.execute("SELECT * FROM instagram_users")
    return print(c.fetchone())

#Upar dados
def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

#Remover dados
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


insert_emp(usuarios)

get_emps_by_name()

print(usuarios)
