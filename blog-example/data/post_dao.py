from data.database_builder import DatabaseBuilder
from werkzeug.exceptions import abort

class PostDao():

    def __init__(self):
        self.db_builder = DatabaseBuilder()
        self.db_builder.build()

    def get_posts(self):
        conn = self.db_builder.get_connection()
        posts = conn.execute("SELECT * FROM posts").fetchall()
        conn.close()

        return posts
    
    def get_post(self, post_id):
        conn = self.db_builder.get_connection()
        post = conn.execute('SELECT * FROM posts WHERE id = ?',
                            (post_id,)).fetchone()
        conn.close()
        if post is None:
            abort(404)
        return post
    
    def create_post(self, title, content):
        conn = self.db_builder.get_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                            (title, content))
        conn.commit()
        conn.close()

    def edit_post(self, post_id, title, content):
        conn = self.db_builder.get_connection()
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                            (title, content, post_id))
        conn.commit()
        conn.close()

    def delete_post(self, post_id):
        conn = self.db_builder.get_connection()
        conn.execute('DELETE FROM posts WHERE id = ?',
                            (post_id,))
        conn.commit()
        conn.close()