from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from app.models import get_all_questions, get_question_by_id, get_next_question_id, init_db

bp = Blueprint('quiz', __name__)

def init_database():
    init_db()

@bp.route('/')
def index():
    db_questions = get_all_questions()

    session["correct_answer"] = 0
    session["total_questions"] = 0

    return render_template("index.html", questions=db_questions)


@bp.route('/question/<int:question_id>', methods = ['GET', 'POST'])
def question(question_id):
    if request.method == "POST":
        correct_answer = get_question_by_id(question_id)["correct_answer"]
        selected_answer = int(request.form.get("answer"))

        session["total_questions"] += 1
        if correct_answer == selected_answer:
            session["correct_answer"] +=1

        return redirect(url_for("quiz.result"))
    
    db_question = get_question_by_id(question_id)

    if db_question:
        return render_template("question.html", question = db_question)
    else:
        redirect(url_for("quiz.index"))


@bp.route('/result')
def result():
    pass