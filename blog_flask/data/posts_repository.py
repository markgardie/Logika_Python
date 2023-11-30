from data.database import get_connection
from werkzeug.exceptions import abort

class PostsRepository():

    def get_posts():
        conn = get_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()

        return posts
    
    def get_post(post_id):
        conn = get_connection()
        post = conn.execute('SELECT * FROM posts WHERE id = ?',
                            (post_id,)).fetchone()
        conn.close()
        if post is None:
            abort(404)
        return post
    
    def create_post(title, content):
        conn = get_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                            (title, content))
        conn.commit()
        conn.close()
