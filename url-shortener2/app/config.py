import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    DATABASE = os.path.join('instance', 'urls.db')
    BASE_URL = 'http://127.0.0.1:5000'