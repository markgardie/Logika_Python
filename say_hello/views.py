from flask import flash, redirect, url_for, render_template
from say_hello import app, db
from say_hello.forms import HelloForm
from say_hello.models import Message

@app.route("/", methods = ["GET", "POST"])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        new_message = Message(name = name, body = body)
        db.session.add(new_message)
        db.session.commit()
        flash("Повідомлення додано успішно")
        return redirect(url_for("index"))
    
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template("index.html", form = form, messages = messages)


