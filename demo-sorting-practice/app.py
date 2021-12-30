from flask import Flask
from flask import render_template, request, redirect
from flask import abort

import db

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route("/")
def index():

    sort_field = request.args.get("sort_field", "id")
    if sort_field not in {"id", "label"}:
        abort(400)

    sort_order = request.args.get("sort_order", "desc")
    if sort_order not in {"asc", "desc"}:
        abort(400)

    bookmarks = db.select_all(sort_field, sort_order)
    return render_template("index.html", bookmarks=bookmarks, sort_order=sort_order, sort_field=sort_field)

@app.route("/add", methods=['POST', 'GET'])
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

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    if request.method == "POST":
        label = request.form["label"]
        url = request.form["url"]
        db.update_bookmark(id, label, url)
        return redirect("/")

    result = db.select_bookmark(id)[0]
    print(result)
    return render_template("edit.html", id=id, label=result[1], url=result[2])


