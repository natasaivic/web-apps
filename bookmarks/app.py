from flask import Flask
from flask import render_template, request, redirect, abort
from datetime import datetime
import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def wall_calendar():
    return datetime.now().strftime('%A %B %d. %Y ')

def wall_clock():
    return datetime.now().strftime('%H:%M')

@app.route("/")
def index():
    # How to implement search by criteria "q"? 
    # 1. How do we know the "q" is sent, and how do we acces it?
    searchword = request.args.get('searchword', '')

    # 2. This won't be db.get_all() anymore but 
    #    it should be something like db.get_by_criteria(), how do we implement it using SQL query?
    if searchword == '':
        order_by = request.args.get("order", "newer")
        if order_by == "older":
            bookmarks=db.get_all("id DESC")
        elif order_by == "newer":
            bookmarks=db.get_all("id ASC")
        else:
            abort(400)
    else:
        bookmarks=db.get_by_searchword(searchword)

    return render_template("index.html", date=wall_calendar(), time=wall_clock(), bookmarks=bookmarks, searchword=searchword)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        label = request.form['label']
        url = request.form['url']
        db.add_bookmark(label, url)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_bookmark(id)
    return redirect("/")

@app.route("/visited/<int:id>")
def visited(id):
    db.mark_as_visited(id)
    return redirect("/")

@app.route("/unvisit/<int:id>")
def unvisit(id):
    db.mark_as_unvisited(id)
    return redirect("/")

@app.route("/edit/<int:id>", methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        label = request.form['label']
        url = request.form['url']
        db.edited_bookmark(id, label, url)

        return redirect("/")
    
    # select label and url where id=id
    results = db.to_be_edited(id)[0]
    return render_template("edit.html", id=id, label=results[0], url=results[1])

