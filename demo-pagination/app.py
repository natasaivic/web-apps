from flask import Flask
from flask import render_template, request, redirect, abort

import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# conn = db.db_connection()
# conn.execute('CREATE TABLE bookmarks_second (id INTEGER PRIMARY KEY AUTOINCREMENT, label TEXT NOT NULL, url TEXT NOT NULL, visited INTEGER NOT NULL)')
# conn.close()

@app.route("/")
def index():
    offset = request.args.get("offset", 0, type=int)
    limit = request.args.get("limit", 3, type=int)

    offset_max = db.max()[0][0]
    bookmarks = db.select_all_bookmarks(offset, limit)
    return render_template("index.html", bookmarks=bookmarks, offset=offset, limit=limit, offset_max=offset_max)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        label = request.form["label"]
        url = request.form["url"]
        db.add_new_bookmark(label, url)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_bookmark(id)
    return redirect("/")