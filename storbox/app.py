import os 
from flask import Flask
from flask import render_template
from flask import request

from flask import flash
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename


app = Flask(__name__)


UPLOAD_FOLDER = './static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = './static/files'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    files = os.listdir(app.config['UPLOAD_PATH']) # f-ja koja ce da izlista fajlove iz ./static/files/ direktorijuma
    print(files)
    return render_template("index.html", files=files)

@app.route("/add", methods=["POST", "GET"])
def add():
    # The application accesses the file from the files dictionary on the request object.
    # use the save() method of the file to save the file permanently somewhere on the filesystem.
    if request.method == "POST":
        # check if the post request has the file part

        file = request.files["file"]

        filename = secure_filename(file.filename)
        full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(full_path)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<filename>")
def delete(filename):
    filename = request.files["file"]
    filename = secure_filename(filename.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.remove(file_path)
    return redirect("/")