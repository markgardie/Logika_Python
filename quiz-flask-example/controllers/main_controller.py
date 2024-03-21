from random import randint
from data.quiz_dao import QuizDao
from flask import session, redirect, url_for, render_template

class MainController():

    def __init__(self):
        self.dao = QuizDao()

    def index(self):
        questions = self.dao.get_all_questions()
        return render_template('index.html', questions = questions)
        
    def quiz(self):
        session["question_id"] = randint(0, 3)
        result = self.dao.get_question(session["question_id"])


        if result is None or len(result) == 0:   
           return redirect(url_for('result'))
        else:
            return '<h1>' + str(result) + '</h1>'
        
    def result(self):
        return "Quiz result"