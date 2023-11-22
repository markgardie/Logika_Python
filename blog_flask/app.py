from flask import Flask, render_template
from data.posts_repository import PostsRepository

app = Flask(__name__)

repository = PostsRepository()

@app.route("/")
def index():
    posts = repository.get_posts()
    return render_template("index.html", posts = posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = repository.get_post(post_id)
    return render_template('post.html', post = post)



