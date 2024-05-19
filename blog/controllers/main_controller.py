from flask import Flask, render_template, request, url_for, flash, redirect
from data.post_repository import PostRepository

class MainController():

    def __init__(self):
        self.repository = PostRepository()

    def index(self):
        pass
    
    def post(self, post_id):
        pass
        
    def create(self):
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]
            self.repository.create_post(title, content)

    def edit(self, post_id):
        pass
    
    def delete(self, post_id):
        pass

    def about(self):
        pass