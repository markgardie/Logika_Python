from data.quiz_database import QuizDatabase


class QuizDao():

    def __init__(self):
        self.db = QuizDatabase()

    def get_all_questions(self):
        self.db.open_db()

        self.db.cursor.execute("SELECT * FROM question")
        result = self.db.cursor.fetchall()

        self.db.close_db()

        return result

    def get_question(self, question_id = 0):
        ''' повертає наступне питання після запитання з переданим id
        для першого запитання передається значення за замовчуванням '''
        self.db.open_db()

        self.db.cursor.execute("SELECT * FROM question WHERE id = ?", 
                               (question_id,))
        result = self.db.cursor.fetchone()

        self.db.close_db()

        return result

