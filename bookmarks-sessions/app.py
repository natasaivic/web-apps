from flask import Flask
from flask import render_template, request, redirect, abort
from flask import session
from datetime import datetime

import hashlib
import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = b'asdasd893asdas15hisr'

def md5(input):
    return hashlib.md5(input.encode()).hexdigest()

def wall_calendar():
    return datetime.now().strftime('%A %B %d. %Y ')

def wall_clock():
    return datetime.now().strftime('%H:%M')

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        
        login_success = db.check_email_and_password(email, md5(password))
        if login_success:
            session['id'] = db.get_user_id(email)
            return redirect("/profile")

    return render_template("login.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        not_registered =  db.check_registar(email)
        if not_registered:
            db.register_user(email, md5(password))
            return redirect("/login")
        else:
            print("This user emal already exists. Try with another email.")
            return redirect("/register")
    
    return render_template("register.html")

@app.route("/profile")
def profile():
    if not 'id' in session:
        return redirect("/")
    
    bookmarks = db.get_bookmarks_by_user(session['id'])
    return render_template("profile.html", bookmarks=bookmarks)

@app.route("/add", methods=["POST", "GET"])
def add():
    if not 'id' in session:
        return redirect("/")

    if request.method == "POST":
        user_id = session['id']
        label = request.form['label']
        url = request.form['url']
        create_on = datetime.now().strftime('%A, %B %d. %Y at %H:%M')

        db.add_bookmark(user_id, label, url, create_on)
        return redirect("/profile")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_bookmark(id)
    return redirect("/profile")

@app.route("/visited/<int:id>")
def visited(id):
    db.mark_as_visited(id)
    return redirect("/")

@app.route("/unvisit/<int:id>")
def unvisit(id):
    db.mark_as_unvisited(id)
    return redirect("/")


@app.route("/logout")
def logout():
    session.pop('id', None)

    return redirect("/login")

@app.route("/feed")
def feed():
    if not 'id' in session:
        return redirect("/")

    bookmarks = db.get_latest_bookmarks()
    return render_template("feed.html", bookmarks=bookmarks)

@app.route("/user_profile/<int:user_id>")
def user_profile(user_id):
    if not 'id' in session:
        return redirect("/")

    if session['id'] == user_id:
        return redirect("/profile")

    bookmarks = db.get_bookmarks_by_user(user_id)
    return render_template("user_profile.html", bookmarks=bookmarks, user_id=user_id)

