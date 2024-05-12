import sqlite3
import os

SCHEMA_PATH = os.path.join(__file__, "..", "schema.sql")
DB_PATH = os.path.join(__file__, "..", "blog.db")

class BlogDatabase():

    def get_connection():
        conn = sqlite3.connect(DB_PATH)
        conn.executescript(SCHEMA_PATH)

        conn.row_factory = sqlite3.Row

        return conn