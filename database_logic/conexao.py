import sqlite3

conn = sqlite3.connect('AA_db.sqlite')

cur = conn.cursor()

#cur.execute('CREATE TABLE pessoas (username VARCHAR)')

#cur.execute('INSERT INTO pessoas(username) values("aquiles")')

cur.execute('SELECT * FROM pessoas')
data = cur.fetchall()
print(data)

conn.commit()


conn.close()
