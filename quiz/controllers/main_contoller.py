from random import randint, shuffle
from data.dao import QuizDao
from flask import session, redirect, url_for, render_template, request


class MainController():

    def __init__(self):
        self.dao = QuizDao()

    def index(self):
        if request.method == "GET":
            questions = self.dao.get_all_questions()
            return render_template("index.html", questions = questions)
        else:
            session["question_id"] = request.form.get("quiz")
            return redirect(url_for("quiz"))
        
    def quiz(self):
        pass
        
    def result(self):
        return render_template("result.html", result = session["result"])