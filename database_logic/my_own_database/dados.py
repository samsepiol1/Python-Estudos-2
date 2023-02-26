import sqlite3
conn = sqlite3.connect('users2.db')
c = conn.cursor()
#c.execute("""CREATE TABLE instagram_users (users) """"")

#with open('saida3.txt') as f:
    #file_data = f.readlines()
    #for line in file_data:
        #line = line.rstrip('\n')
def insert_emp(name_arc):
    with conn:
        name_arc = str(name_arc)
        with open(name_arc) as f:
            file_data = f.readlines()
            for line in file_data:
                line = line.rstrip('\n')
                c.execute("INSERT INTO instagram_users VALUES (:users)", {'users':line})

insert_emp('seguidores_alguem.txt')
def get_emps_by_name():
    c.execute("SELECT * FROM instagram_users")
    y = c.fetchall()
    z = set(y)
    for x in z:
        a = tuple(x)
        print(a)


get_emps_by_name()


