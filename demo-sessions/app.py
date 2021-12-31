from flask import Flask
from flask import request
from flask import session
from flask import redirect, render_template

import hashlib, db
from datetime import datetime


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = b'asdasd893asdas15hisr'


def md5(input):
    """
    Returns a MD5 hash of the string.
        md5("nata1") -> 2ecface7be4ff3017ac0989971fb7e69
    """
    return hashlib.md5(input.encode()).hexdigest()

@app.route("/")
def index():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        db.register_user(email, md5(password))
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        login_success = db.check_loging(email, md5(password))
        if login_success:
            session['id'] = db.get_user_id(email)
            return redirect("/profile")

        return redirect("/login")
        
    return render_template("login.html")


@app.route("/profile")
def profile():
    if not 'id' in session:
        return redirect("/")

    tweets = db.get_tweets_by_user(session['id'])
    return render_template("profile.html", tweets=tweets)


@app.route("/user_profile/<int:user_id>")
def user_profile(user_id):
    if not 'id' in session:
        return redirect("/")

    if session['id'] == user_id:
        return redirect("/profile")

    tweets = db.get_tweets_by_user(user_id)
    return render_template("user_profile.html", tweets=tweets, user_id=user_id)


@app.route("/tweet", methods=["GET", "POST"])
def tweet():
    if not 'id' in session:
        return redirect("/")

    if request.method == "POST":
        user_id = session['id']
        tweet = request.form['tweet']
        create_on = datetime.now().strftime('%A, %B %d. %Y at %H:%M')

        db.create_new_tweet(user_id, tweet, create_on)
        return redirect("/profile")

    return render_template("tweet.html")


@app.route("/logout")
def logout():
    session.pop('id', None)

    return redirect("/login")


@app.route("/feed")
def feed():
    if not 'id' in session:
        return redirect("/")

    tweets = db.get_latest_tweets()
    return render_template("feed.html", tweets=tweets)