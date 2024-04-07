from flask import Flask, render_template, request, url_for, flash, redirect
from data.posts_dao import PostDao

class MainController():

    def __init__(self):
        self.dao = PostDao

    def index(self):
        posts = self.dao.get_posts()
        return render_template("index.html", posts = posts)
    

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
    
    def delete(self, id):
        if request.method == "POST":
            self.dao.delete_post(id)
            return redirect(url_for("index"))
        
        return render_template("delete.html")

    def about(self):
        return render_template("about.html")