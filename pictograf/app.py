import os
import logging

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import session
import hashlib
from datetime import datetime

import imagelib
import db


app = Flask(__name__)

# setup template reload (no caching)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# setup session secret key
app.secret_key = b"asdasd893asdas15hisr"

# setup image uploads
UPLOAD_FOLDER = "./static/files"
ALLOWED_EXTENSIONS = {"txt", "jpg", "png", "pdf", "jpeg", "gif"}
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER

# setup logger
logging.basicConfig(
    encoding="utf-8", level=logging.INFO, format="%(asctime)s %(message)s"
)


def md5(input):
    return hashlib.md5(input.encode()).hexdigest()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


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
            session["id"] = db.get_user_id(email)
            session["name"] = db.get_user_first_name(email)
            session["surname"] = db.get_user_last_name(email)
            session["profile_pic"] = db.get_user_profile_pic(email)
            return redirect("/profile")
        else:
            logging.info("This profile does not exist. Try register first.")
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
    if not "id" in session:
        return redirect("/")

    posts = db.get_posts_by_user(session["id"])
    
    post_comments = {}
    for post in posts:
        post_comments[post[0]] = db.get_comments_by_post(post[0])

    info = db.get_info_by_user(session["id"])
    print(info)
    return render_template("profile.html", posts=posts, post_comments=post_comments, info = info)

@app.route("/comment/<int:post_id>", methods=["POST"])
def comment(post_id):
    if not 'id' in session:
        return redirect("/")

    if request.method == "POST":
        comment = request.form["comment"]

        user_id = session["id"]
        created_on = datetime.now().strftime("%b %d. %Y at %H:%M")
        db.save_new_comment(user_id, post_id, comment, created_on)
    
    return redirect(request.referrer)

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_comment(id)
    return redirect("/profile")

@app.route("/feed")
def feed():
    if not "id" in session:
        return redirect("/")

    posts = db.get_latest_posts()
    # SELECT user_id, image_file, caption, create_on, profile_pic, posts.id

    post_comments = {}
    for post in posts:
        post_comments[post[5]] = db.get_comments_by_post(post[5])


    return render_template("feed.html", posts=posts, post_comments=post_comments)


@app.route("/post", methods=["POST", "GET"])
def post():
    if not "id" in session:
        logging.error(
            f"User tried to access forbidden area!! The user came from {request.remote_addr}"
        )
        return redirect("/")

    if request.method == "POST" and request.files:
        image = request.files["image"]
        file_name = md5(f"{image.filename}-{datetime.now()}")
        file_name = f"{file_name}.jpg"
        file_full_path = os.path.join(app.config["IMAGE_UPLOADS"], file_name)

        image.save(file_full_path)
        logging.info("Image saved.")

        imagelib.resize(file_full_path)
        logging.info("Image resized.")

        user_id = session["id"]
        caption = request.form["caption"]
        create_on = datetime.now().strftime("%A, %B %d. %Y at %H:%M")
        db.save_new_post(user_id, file_name, caption, create_on)      
        logging.info("Post saved.")

        logging.debug(image)

        return redirect("/profile")

    return render_template("post.html")


@app.route("/logout")
def logout():
    session.pop("id", None)

    return redirect("/login")


@app.route("/user_profile/<int:user_id>")
def user_profile(user_id):
    if not "id" in session:
        return redirect("/")

    if session["id"] == user_id:
        return redirect("/profile")

    posts = db.get_posts_by_user(user_id)
    first_name = db.get_profile_first_name(user_id)
    last_name = db.get_profile_last_name(user_id)
    profile_pic = db.get_profile_profile_pic(user_id)
    
    post_comments = {}
    for post in posts:
        post_comments[post[0]] = db.get_comments_by_post(post[0])

    return render_template(
        "user_profile.html",
        posts=posts,
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        profile_pic=profile_pic,
        post_comments=post_comments
    )


@app.route("/edit_profile_pic", methods=["POST", "GET"])
def edit_profile_pic():
    if not "id" in session:
        return redirect("/")

    if request.method == "POST" and request.files:
        image = request.files["image"]
            
        file_name = f"{session['id']}.jpg"
        file_full_path = os.path.join(f"static/profile-pics/{file_name}")
        image.save(file_full_path)
        imagelib.resize(file_full_path)
        db.update_profile_pic(session['id'], file_name)

        return redirect("/profile")
    
    return render_template("edit_profile_pic.html")


@app.route("/edit_profile", methods=["POST", "GET"])
def edit_profile():
    if not "id" in session:
        return redirect("/")
    
    if request.method == "POST":
        current_city = request.form["current_city"]
        hometown = request.form["hometown"]
        bio = request.form["bio"]
        db.save_info(session["id"], current_city, hometown, bio)

        return redirect("/profile")

    return render_template("edit_profile.html")


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if not "id" in session:
        return redirect("/")
    
    if request.method == "POST":
        old_password = request.form["old_password"]
        match = db.match_old_password(session["id"], md5(old_password))
        if match is True:
            new_password = request.form["new_password"]
            new_password_re_enter = request.form["new_password_re_enter"]
            if new_password == new_password_re_enter:
                db.update_new_password(session["id"], md5(new_password))
        else:
            return redirect("/profile")

    return render_template("settings.html")
