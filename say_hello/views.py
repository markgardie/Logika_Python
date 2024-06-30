from flask import flash, redirect, url_for, render_template
from say_hello import app, db
from say_hello.forms import HelloForm
from say_hello.models import Message

@app.route("/", methods = ["GET", "POST"])
def index():
    pass