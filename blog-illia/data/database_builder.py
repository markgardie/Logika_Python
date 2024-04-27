import sqlite3
import os

SCHEMA_PATH = os.path.join(__file__, "..", "schema.sql")
DB_PATH = os.path.join(__file__, "..", "blog.db")

class DatabaseBuilder():

    def build(self):

        conn = sqlite3.connect(DB_PATH)

        with open(SCHEMA_PATH) as f:
            script = f.read()
            conn.executescript(script) 

    def get_connection(self):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn