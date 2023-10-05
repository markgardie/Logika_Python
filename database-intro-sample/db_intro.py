import sqlite3

conn = sqlite3.connect("database-intro-sample\intro.db")
cursor = conn.cursor()



res = cursor.execute(''' 
    SELECT * FROM students WHERE avg_mark >= 10
''')

print(res.fetchall())