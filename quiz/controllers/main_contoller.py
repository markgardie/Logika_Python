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
        if not ('question_id' in session) or int(session["question_id"]) < 0:
            return redirect(url_for("index"))
        else:
            question = self.dao.get_question(session["question_id"])

            if request.method == "POST":
                answer = request.form.get("ans_text")
                if answer == question[2]:
                    session["result"] = "Відповідь правильна"
                else:
                    session["result"] = "Відповідь неправильна"
            else:
                answers = list(question[2:])
                shuffle(answers)
                return render_template("quiz.html", question = question, answer_list = answers)
        
    def result(self):
        return render_template("result.html", result = session["result"])