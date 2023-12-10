from data.database import get_connection
from werkzeug.exceptions import abort

class PostsRepository():

    def get_posts():
        conn = get_connection()
        posts = conn.execute("SELECT * FROM posts").fetchall()
        conn.close()

        return posts
    
    def edit_post(post_id, title, content):
        conn = get_connection()
        conn.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?",
                     (title, content, post_id))
        conn.commit()
        conn.close()

    def delete_post(post_id):
        conn = get_connection()
        conn.execute("DELETE FROM posts WHERE id = ?",
                     (post_id,))
        conn.commit()
        conn.close()