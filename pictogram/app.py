import os

from flask import Flask
from flask import render_template, redirect, request

import db
import queries

# conn = db.db_connection()
# conn.execute(queries.users())
# conn.close()

app = Flask(__name__)

UPLOAD_FOLDER = './static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        description = request.form['description']
        print(description)
    files = os.listdir(app.config['IMAGE_UPLOADS'])
    return render_template("index.html", files = files, description=description)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        db.new_sign_up(email)
        return redirect("/")

    return render_template("login.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        if request.files:
            image = request.files['image']
            request.form['description']
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
        return redirect("/")

    return render_template("profile.html")
