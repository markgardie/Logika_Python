from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from app.models import get_all_questions, get_question_by_id, get_next_question_id, init_db

bp = Blueprint('quiz', __name__)

@bp.before_app_first_request
def initialize_database():
    pass

@bp.route('/')
def index():
    pass

@bp.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    pass


@bp.route('/result')
def result():
    pass