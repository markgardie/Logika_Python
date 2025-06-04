from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from app.models import get_all_questions, get_question_by_id, get_next_question_id, init_db

bp = Blueprint('quiz', __name__)

@bp.before_app_request
def initialize_database():
    """Ініціалізація бази даних перед першим запитом."""
    init_db()

@bp.route('/')
def index():
    """Головна сторінка зі списком питань."""
    # Отримуємо всі питання
    questions = get_all_questions()
    
    # Скидаємо лічильник правильних відповідей при запуску нової вікторини
    session['correct_answers'] = 0
    session['total_questions'] = 0
    
    return render_template('index.html', questions=questions)

@bp.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    """Сторінка з питанням."""
    if request.method == 'POST':
        # Отримуємо відповідь користувача і перевіряємо її
        q = get_question_by_id(question_id)
        
        selected_option = int(request.form.get('answer'))
        correct_answer = q['correct_answer']
        
        # Збільшуємо лічильники
        session['total_questions'] = session.get('total_questions', 0) + 1
        if selected_option == correct_answer:
            session['correct_answers'] = session.get('correct_answers', 0) + 1
        
        # Перенаправляємо на наступне питання або на сторінку результатів
        next_question_id = get_next_question_id(question_id)
        
        if next_question_id:
            return redirect(url_for('quiz.question', question_id=next_question_id))
        else:
            return redirect(url_for('quiz.result'))
    
    # Якщо це GET запит, показуємо питання
    q = get_question_by_id(question_id)
    
    if q:
        return render_template('question.html', question=q)
    else:
        return redirect(url_for('quiz.index'))

@bp.route('/result')
def result():
    """Сторінка з результатами."""
    correct = session.get('correct_answers', 0)
    total = session.get('total_questions', 0)
    percentage = (correct / total * 100) if total > 0 else 0
    
    return render_template('result.html', correct=correct, total=total, percentage=percentage)