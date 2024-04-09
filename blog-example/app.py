from flask import Flask
from routes import BlogRoutes

class BlogApp(Flask):

    def __init__(self):
        super().__init__(__name__)
        self.router = BlogRoutes()
        self.router.setup_routes(self)
        self.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == "__main__":
    app = BlogApp()
    app.run()