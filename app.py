#imports
from flask import Flask ,request ,redirect ,render_template ,session
from flask_session import Session
from werkzeug.security import check_password_hash
from helpers import apology 
import sqlite3 as sql


#conf application
app = Flask(__name__)

#auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Session conf
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#database configuration
con = sql.connect("flask-test.db",check_same_thread=False)
con.row_factory = sql.Row
db = con.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# @app.route("/")
# @login_requierd   #TODO
# def index()

#login
@app.route("/login" ,methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
    #TODO
    #Ensure about valid inputs
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")).fetchall()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")
