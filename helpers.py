from flask import render_template

def apology(message,code=400):
    return render_template("apology.html" , code=code , message=message), code