import sqlite3

path = r"D:\Mark\Desktop\Logika_Python\web_db\artists.db"

conn = sqlite3.connect(path)
cursor = conn.cursor()

# Скільки художників
cursor.execute("SELECT * FROM artists")
data = cursor.fetchall()
print(len(data))
