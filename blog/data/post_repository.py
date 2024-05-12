from data.database import BlogDatabase
from werkzeug.exceptions import abort

class PostRepository():

    def __init__(self):
        self.db = BlogDatabase()

    def get_posts(self):
        pass

    def get_post(self, id):
        pass

    def create_post(self, title, content):
        conn = self.db.get_connection()
        conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        conn.close()

    def delete_post(self, id):
        pass

    def update_post(self, id, title, content):
        pass
