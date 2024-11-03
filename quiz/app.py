from flask import Flask
from routes import setup_routes

app = Flask(__name__)
setup_routes(app)
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == '__main__':
   app.run()
   