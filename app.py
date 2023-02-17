from flask import Flask, render_template , session
from cs50 import SQL
from helpers import apology, login_required
from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///base.db")


@app.route("/")
def index():
    return render_template("index.html")