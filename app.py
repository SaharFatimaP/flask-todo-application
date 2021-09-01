from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import redirect

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///toto.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    # date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/", methods=["GET", "POST"])
def helloWorld():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
#
        todo = Todo(title=title, desc=desc)  # object of Todo model
        db.session.add(todo)
        db.session.commit()
    return render_template("index.html")


@app.route("/todos")
def todos():
    todolist = Todo.query.all()
    return render_template("todos.html", todolist=todolist)


@app.route("/update/<int:sno>",  methods=["GET", "POST"])
def update(sno):
    if (request.method == 'POST'):
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/todos")
    todolist = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todolist=todolist)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/todos")


if (__name__ == "__main__"):
    app.run(debug=True)
