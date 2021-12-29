from flask import Flask
from flask import render_template, redirect, request, abort

import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# conn = db.db_connection()
# conn.execute('CREATE TABLE bookmarks (id INTEGER PRIMARY KEY AUTOINCREMENT, label TEXT NOT NULL, url_ TEXT NOT NULL, visited INTEGER NOT NULL)')
# conn.close()

@app.route("/")
def index():
    sort_field = request.args.get("sort_field", "id") # NOTE: default value
    if not sort_field in {"id", "label"}:
        abort(400)

    sort_order = request.args.get("sort_order", "desc") # NOTE: default value
    if not sort_order in {"asc", "desc"}:
        abort(400)
    
    bookmarks = db.list_all(sort_field, sort_order)
    return render_template("index.html", bookmarks=bookmarks, sort_order=sort_order, sort_field=sort_field)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        label = request.form["label"]
        url = request.form["url"]
        db.add_bookmark(label, url)
        return redirect("/")

    return render_template("add.html")
