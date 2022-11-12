#imports
from flask import Flask
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

