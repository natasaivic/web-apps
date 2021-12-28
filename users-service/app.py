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
        email = request.form['email'] # form: The form parameters.
        password = md5(request.form['password'])

        # check db, if 0 results, then the username / password is wrong, 
        # otherwise -> redirect to somewhere where they should be
        is_valid = db.check_loging(email, password)
        if is_valid == True:
            return redirect("/profile")
        error = "Wrong username and password combination"

    return render_template("index.html", error=error, request=request)


@app.route("/register", methods=["POST", "GET"])
def register():
    error = None 

    if request.method == "POST":
        firstname = request.form['firstname']
        surname = request.form['surname']
        email = request.form['email']
        password = md5(request.form['password'])

        is_existing = db.check_existing_email(email)
        if is_existing == True:
            error = "This email is already taken. Use different email."
            return render_template("register.html", error=error)
        
        db.create_new_user_account(firstname, surname, email, password)
        return redirect("/?reg=true")

    return render_template("register.html", error=error)

@app.route("/profile")
def profile():
    return render_template("profile.html")