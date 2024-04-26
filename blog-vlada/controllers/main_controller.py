from flask import Flask, render_template, request, url_for, flash, redirect
from data.post_dao import PostDao

class MainController():

    def __init__(self):
        self.dao = PostDao()

    def index(self):
        posts = self.dao.get_posts()
        return render_template("index.html", posts = posts)
    
    def post(self, post_id):
        post = self.dao.get_post(post_id)
        return render_template('post.html', post = post)
        
    def create(self):
        
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]

            if title != "":
                self.dao.create_post(title, content)
                return redirect(url_for("index"))
            else:
                flash("Неправильний заголовок")

        return render_template("create.html")
    
    def edit(self, post_id):
        post = self.dao.get_post(post_id)

        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            else:
                self.dao.edit_post(post_id, title, content)
                return redirect(url_for('index'))
            
        return render_template('edit.html', post = post)
    
    def delete(self, post_id):
        if request.method == "POST":
            self.dao.delete_post(post_id)
            return redirect(url_for("index"))
        
        return render_template("delete.html")

    def about(self):
        return render_template("about.html")