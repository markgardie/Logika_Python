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
        conn = self.db.get_connection()
        conn.execute("DELETE FROM posts WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update_post(self, id, title, content):
        conn = self.db.get_connection()
        conn.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", 
                     (title, content, id))
        conn.commit()
        conn.close()
