
from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    # Реєстрація маршрутів
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app