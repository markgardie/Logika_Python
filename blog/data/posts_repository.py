from data.database import get_connection
from werkzeug.exceptions import abort

class PostsRepository():

    def get_posts():
        conn = get_connection()
        posts = conn.execute("SELECT * FROM posts").fetchall()
        conn.close()

        return posts