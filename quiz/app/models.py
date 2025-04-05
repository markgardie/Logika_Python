import sqlite3
import os
from flask import current_app, g


def get_db():
    if not os.path.exists(current_app.instance_path):
        os.makedirs(current_app.instance_path)
    

    db_path = os.path.join(current_app.instance_path, 'quiz.db')

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS questions(
                id INTEGER PRIMARY KEY,
                question TEXT NOT NULL,
                option1 TEXT NOT NULL,
                option2 TEXT NOT NULL,
                option3 TEXT NOT NULL,
                option4 TEXT NOT NULL,
                correct_answer INTEGER NOT NULL
            )
        '''
    )

    question_count = cursor.execute("SELECT COUNT(*) FROM questions").fetchone()[0]

    if question_count == 0:
        sample_questions = [
            ('Яка столиця України?', 'Львів', 'Київ', 'Харків', 'Одеса', 2),
            ('Скільки планет у Сонячній системі?', '7', '8', '9', '10', 2),
            ('Яка найдовша річка у світі?', 'Амазонка', 'Ніл', 'Дніпро', 'Міссісіпі', 2),
            ('Хто написав "Кобзар"?', 'Іван Франко', 'Тарас Шевченко', 'Леся Українка', 'Іван Котляревський', 2),
            ('Символом якої країни є клен?', 'Україна', 'США', 'Канада', 'Японія', 3)
        ]

        cursor.executemany('''
            INSERT INTO questions (question, option1, option2, option3, option4, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_questions)

    db.commit()
    

def close_db():
    pass

def init_db():
    pass

def get_all_questions():
    pass

def get_question_by_id():
    pass