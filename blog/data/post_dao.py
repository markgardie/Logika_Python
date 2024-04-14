from data.database_builder import DatabaseBuilder
from werkzeug.exceptions import abort

class PostDao():

    def __init__(self):
        self.db_builder = DatabaseBuilder()
        self.db_builder.build()

    def get_post(self, id):
        self.conn = self.db_builder.get_connection()

        post = self.conn.execute("SELECT * FROM posts WHERE id = ?", (id,)).fetchone()

        self.conn.close()

        return post