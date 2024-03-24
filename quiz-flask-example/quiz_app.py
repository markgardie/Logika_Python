from flask import Flask
from quiz_routes import setup_routes

app = Flask(__name__)
setup_routes(app)
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
   app.run()
   
