from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite3:///relationship.db"


@app.route("/")
def helloWorld():
    return("Hello World")


if (__name__ == "__main__"):
    app.run(debug=True)
