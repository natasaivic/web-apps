import os
from flask import Flask
from flask import render_template, request, redirect


app = Flask(__name__)


UPLOAD_FOLDER = './static/files'
ALLOWED_EXTENSIONS = {'txt', 'jpg', 'png', 'pdf', 'jpeg', 'gif'}
app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    files = os.listdir(app.config['IMAGE_UPLOADS'])
    return render_template("index.html", files=files)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
            print("Image saved.")
            return redirect("/")

    return render_template("add.html")