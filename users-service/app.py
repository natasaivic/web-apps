from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from utils import md5
import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=["POST", "GET"])
def index():
    error = None
    
    if request.method == "POST":
        email = request.form['email']
        password = md5(request.form['password'])

        # check db, if 0 results, then the username / password is wrong, 
        # otherwise -> redirect to somewhere where they should be
        is_valid = db.check_loging(email, password)
        if is_valid == True:
            return redirect("/profile")
        error = "Wrong username and password combination"

    return render_template("index.html", error=error)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    error = None 

    if request.method == "POST":
        request.form['name']
        request.form['surname']
        email = request.form['email']
        md5(request.form['password'])

        is_existing = db.check_signing(email)
        if is_existing != True:
            return redirect("/profile")
        error = "This email is already taken. Use different email."

    return render_template("signup.html", error=error)