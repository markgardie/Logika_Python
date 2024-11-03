import sqlite3

class QuizDatabase():

    
    def __init__(self):
        self.db_name = 'quiz-flask-example\data\quiz.sqlite'
        self.conn = None
        self.cursor = None

    def open_db(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def do(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def create_tables(self):
        self.open_db()
        self.cursor.execute('''PRAGMA foreign_keys=on''')

        self.do('''CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY,
                question VARCHAR,
                answer VARCHAR,
                wrong1 VARCHAR,
                wrong2 VARCHAR,
                wrong3 VARCHAR)''')

        
        self.close_db()

    def add_questions(self):

        questions = [
            ('Скільки місяців на рік мають 28 днів?', 'Всі', 'Один', 'Жодного', 'Два'),
            ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрим', 'Червоним', 'Не зміниться', 'Фіолетовим'),
            ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Любою'),
            ('Що не має довжини, глибини, ширини, висоти, а можна виміряти?', 'Час', 'Дурність', 'Море', 'Повітря'),
            ('Коли сіткою можна витягнути воду?', 'Коли вода замерзла', 'Коли немає риби', 'Коли спливла золота рибка', 'Коли сітка порвалася'),
            ('Що більше слона і нічого не важить?', 'Тінь слона', 'Повітряна куля', 'Парашут', 'Хмара')
        ]

        self.open_db()

        self.cursor.executemany('''
                            INSERT INTO question (question, answer, wrong1, wrong2, wrong3)
                            VALUES (?, ?, ?, ?, ?)
                            ''', questions)
        
        self.conn.commit()

        self.close_db()