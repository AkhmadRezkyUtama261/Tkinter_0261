import sqlite3
con = sqlite3.connect('Tutorial.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, "\
"name TEXT, age INTEGER)")
cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice",21))
cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob",22))
con.commit()
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
con.close()