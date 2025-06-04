import sqlite3
import os
from flask import current_app, g

def get_db():
    """Підключення до бази даних."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            os.path.join(current_app.instance_path, 'quiz.db'),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Закриття з'єднання з базою даних."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Ініціалізація бази даних."""
    # Перевіряємо чи існує директорія instance
    if not os.path.exists(current_app.instance_path):
        os.makedirs(current_app.instance_path)
    
    # Перевіряємо чи існує файл бази даних
    db_path = os.path.join(current_app.instance_path, 'quiz.db')
    
    db = get_db()
    cursor = db.cursor()
    
    # Створюємо таблицю питань
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        correct_answer INTEGER NOT NULL
    )
    ''')
    
    # Перевіряємо чи є вже питання в базі
    question_count = cursor.execute('SELECT COUNT(*) FROM questions').fetchone()[0]
    
    # Якщо питань немає, додаємо декілька прикладів
    if question_count == 0:
        sample_questions = [
            ('Яка столиця України?', 'Львів', 'Київ', 'Харків', 'Одеса', 2),
            ('Скільки планет у Сонячній системі?', '7', '8', '9', '10', 2),
            ('Яка найдовша річка у світі?', 'Амазонка', 'Ніл', 'Дніпро', 'Міссісіпі', 2),
            ('Хто написав "Кобзар"?', 'Іван Франко', 'Тарас Шевченко', 'Леся Українка', 'Іван Котляревський', 2),
            ('Символом якої країни є клен?', 'Україна', 'США', 'Канада', 'Японія', 3)
        ]
        
        cursor.executemany('INSERT INTO questions (question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?)', sample_questions)
    
    db.commit()

# Функції для роботи з питаннями
def get_all_questions():
    """Отримати всі питання."""
    db = get_db()
    questions = db.execute('SELECT id, question FROM questions').fetchall()
    return questions

def get_question_by_id(question_id):
    """Отримати питання за ідентифікатором."""
    db = get_db()
    question = db.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
    return question

def get_next_question_id(current_id):
    """Отримати ідентифікатор наступного питання."""
    db = get_db()
    next_question = db.execute(
        'SELECT id FROM questions WHERE id > ? ORDER BY id ASC LIMIT 1', 
        (current_id,)
    ).fetchone()
    return next_question['id'] if next_question else None