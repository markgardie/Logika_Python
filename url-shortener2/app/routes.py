from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, abort
from app.models import URL
from app.services import create_short_url
import validators

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
   if request.method == "POST":
       original_url = request.form.get('url')

       if not validators.url(original_url):
           return render_template('index.html', 
                                  error = 'Введіть коректний URL',
                                  original_url = original_url)
       
       short_code = create_short_url(original_url)
       short_url = f"{current_app.config['BASE_URL']}/{short_code}"

       return render_template('index.html', 
                              short_url = short_url,
                                original_url = original_url)
   return render_template('index.html')


@main.route('/<short_code>')
def redirect_to_url(short_code):
    url_data = URL.get_by_short_code(short_code)

    if url_data is None:
        abort(404)

    URL.increment_clicks(short_code)

    return redirect(url_data['original_url'])

@main.route('/stats')
def stats():
    urls = URL.get_all()
    base_url = current_app.config['BASE_URL']

    return render_template('stats.html', urls = urls, base_url = base_url)

@main.route('/info/<short_code>')
def url_info(short_code):
    url_data = URL.get_by_short_code(short_code)

    if url_data is None:
        abort(404)

    base_url = current_app.config['BASE_URL']

    short_url = f"{base_url}/{short_code}"

    return render_template('url_info', url = url_data, short_url = short_url)

@main.errorhandler(404)
def page_not_found(e):
    pass