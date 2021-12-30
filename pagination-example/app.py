from flask import Flask
from flask import render_template, request, redirect, abort

import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# conn = db.db_connection()
# conn.execute('CREATE TABLE bookmarks (id INTEGER PRIMARY KEY AUTOINCREMENT, label TEXT NOT NULL, url TEXT NOT NULL, visited INTEGER NOT NULL)')
# conn.close()

@app.route("/")
def index():
    offset = request.args.get("offset", 0, type=int) # IMPORATNT: Default value is HERE!
    limit = request.args.get("limit", 3, type=int)

    # if not limit in {3, 4, 10, 30}:
    #     limit = 3
    bookmarks = db.select_all(offset, limit)

    return render_template("index.html", bookmarks=bookmarks, offset=offset, limit=limit)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        label = request.form["label"]
        url = request.form["url"]
        db.add_new_bookmark(label, url)
        return redirect("/")

    return render_template("add.html")


# <a href="/delete/{{bookmark[0]}}>delete</a>
@app.route("/delete/<int:id>")
def delete(id):
    db.delete_bookmark(id)
    return redirect("/")


# <a href="/delete?id={{bookmark[0]}}>delete</a>
# @app.route("/delete")
# def delete():
#     id = request.args.get("id", -1, type=int)
#     db.delete_bookmark(id)

#     return redirect("/")