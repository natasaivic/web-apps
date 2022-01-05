import os

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import session
import hashlib
import datetime

import db

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = b'asdasd893asdas15hisr'

UPLOAD_FOLDER = './static/files'
ALLOWED_EXTENSIONS = {'txt', 'jpg', 'png', 'pdf', 'jpeg', 'gif'}
app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER


def md5(input):
    return hashlib.md5(input.encode()).hexdigest()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # check if email&password exists in registrar
        login_sucessful = db.check_email_and_password(email, md5(password))
        if login_sucessful:
            # kreiraj sesiju
            session['id'] = db.get_user_id(email)
            session['name'] = db.get_user_first_name(email)
            session['surname'] = db.get_user_last_name(email)
            return redirect("/profile")
        else:
            print("This profile does not exist. Try register first.")
            return redirect("/login")

    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]

        not_registered = db.check_email_in_registrar(email)
        if not_registered:
            db.new_user_registration(name, surname, email, md5(password))
            return redirect("/login")
        else:
            return redirect("/register?error=This email is taken. Try another.")

    return render_template("register.html")

@app.route("/profile")
def profile():
    if not 'id' in session:
        return redirect("/")

    posts = db.get_posts_by_user(session['id'])
    return render_template("profile.html", posts=posts)

@app.route("/feed")
def feed():
    if not 'id' in session:
        return redirect("/")
    
    return render_template("feed.html")

@app.route("/post", methods=["POST", "GET"])
def post():
    if not 'id' in session:
        return redirect("/")

    if request.method == "POST" and request.files:
        user_id = session['id']
        image = request.files["image"]
        image_file = md5(f"{image.filename}-{datetime.datetime.now()}")
        image_file = f"{image_file}.jpg"
        image.save(os.path.join(app.config['IMAGE_UPLOADS'], image_file))
        print("Image saved.")

        caption = request.form["caption"]
        db.save_new_post(user_id, image_file, caption)

        return redirect("/profile")

    return render_template("post.html")

@app.route("/logout")
def logout():
    session.pop('id', None)
    
    return redirect("/login")
    