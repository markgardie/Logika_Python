from flask import Flask, render_template, request, url_for, flash, redirect
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

@app.route('/create')
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            repository.create_post(title, content)
            return redirect(url_for('index'))
        
    return render_template('create.html')

