#imports
from flask import Flask ,request ,redirect ,render_template
from flask import SQLAlchemy
from flask_session import Session
from helpers import db_conf

#conf application
app = Flask(__name__)

#auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Session conf
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#TODO 
#config database

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
    Session.clear()
    if request.method == "POST":
        #TODO
        #Ensure about valid inputs

        #TODO
        # Remember which user has logged in
        return redirect("/")
    else:
        return render_template("login.html")
