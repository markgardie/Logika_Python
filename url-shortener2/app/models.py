import sqlite3
from flask import current_app, g
import datetime

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()


class URL:
    @staticmethod
    def create(original_url, short_code):
       db = get_db()
       cursor = db.cursor()

       cursor.execute(
           "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
           (original_url, short_code)
       )
       db.commit()
       return cursor.lastrowid
    
    @staticmethod
    def get_by_short_code(short_code):
       pass
    
    @staticmethod
    def increment_clicks(short_code):
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?",
            (short_code,)
        )

        db.commit()
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        urls = cursor.execute("SELECT * FROM urls").fetchall()
        return urls