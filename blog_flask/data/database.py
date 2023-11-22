import sqlite3

SCHEMA_PATH = r"blog_flask\data\schema.sql"
DB_NAME = "blog.db"

def build():

    conn = sqlite3.connect(DB_NAME)

    with open(SCHEMA_PATH) as f:
        script = f.read()
        conn.executescript(script) 

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

