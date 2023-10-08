import sqlite3

conn = sqlite3.connect(r"db_intro\intro_db.db")
cursor = conn.cursor()

cursor.execute('''   

    INSERT INTO students (name, surname, mark, class)
    VALUES ("John", "Smith", 10, "11-B")

''')

cursor.execute('''   

    INSERT INTO students (name, surname, mark, class)
    VALUES ("Jane", "Doe", 7, "10-A")

''')

res = cursor.execute('''   

    SELECT * FROM students

''')

conn.commit()

print(res.fetchall())
               