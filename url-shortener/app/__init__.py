from flask import Flask
from app.config import Config
import os
import sqlite3

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    # Переконаємося, що директорія для екземпляра існує
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Ініціалізуємо базу даних
    with app.app_context():
        init_db()
    
    # Реєструємо маршрути
    from app.routes import main
    app.register_blueprint(main)
    
    return app

def init_db():
    conn = sqlite3.connect('instance/urls.db')
    cursor = conn.cursor()
    
    # Створюємо таблицю, якщо вона не існує
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_code TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        clicks INTEGER DEFAULT 0
    )
    ''')
    
    conn.commit()
    conn.close()