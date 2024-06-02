from flask import Flask, render_template, request, url_for, flash, redirect
from data.post_repository import PostRepository

class MainController():

    def __init__(self):
        self.repository = PostRepository()

    def index(self):
        posts = self.repository.get_posts()
        render_template("index.html", posts = posts)
    
    def post(self, post_id):
        post = self.repository.get_post(post_id)
        render_template("post.html", post = post)
        
    def create(self):
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]
    
            if title != "":
                self.repository.create_post(title, content)
                redirect(url_for("index"))
            else:
                flash("Пустий заголовок")
        else:
            return render_template("create.html")

    def edit(self, post_id):
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]
    
            if title != "":
                self.repository.update_post(post_id, title, content)
                redirect(url_for("index"))
            else:
                flash("Пустий заголовок")
        else:
            post = self.repository.get_post(post_id)
            return render_template("edit.html", post = post)
    
    def delete(self, post_id):
        pass

    def about(self):
        pass