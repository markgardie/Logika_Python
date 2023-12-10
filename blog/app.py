from flask import Flask

app = Flask(__name__)

repository = PostsRepository()

@app.route("/")
def index():
    return "Hello World"

@app.route("/edit/<int:post_id>")
def edit(post_id):
    post = repository.get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            repository.edit_post(post_id, title, content)
            return redirect(url_for('index'))
        
    return render_template('edit.html', post = post)

@app.route("/delete/<int:post_id>")
def delete(post_id):
    if request.method == 'POST':
        repository.delete_post(post_id)
        return redirect(url_for('index'))
    
    return render_template('delete.html')