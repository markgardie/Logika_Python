import sqlite3

path = r"D:\Mark\Desktop\Logika_Python\db_lesson1\artists.db"

conn = sqlite3.connect(path)
cursor = conn.cursor()

# Скільки художників
cursor.execute("SELECT * FROM artists")
data = cursor.fetchall()
print(len(data))


# Ім'я найстаршого художника
cursor.execute('SELECT Name FROM artists WHERE "Birth Year" < 1900 ORDER BY "Birth Year" ')
data = cursor.fetchone()
print(data)