from flask import Flask
from flask import request
from flask.templating import render_template

import db
import queries
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    # How to implement search by criteria "q"? 
    # 1. How do we know the "q" is sent, and how do we acces it?
    searchword = request.args.get('searchword', '')
    # 2. This won't be db.get_reminders() anymore but 
    #    it should be something like db.get_by_criteria(), how do we implement it using SQL query?
    if searchword == '':
        quotes = db.get_all_quotes()
    else:
        quotes = db.select_by_searchword(searchword)

    return render_template("index.html", quotes=quotes, searchword=searchword)

@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        author = request.form["author"]
        quote = request.form["quote"]
        db.add_quote(author, quote)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_quote(id)
    return redirect("/")

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    if request.method == "POST":
        author = request.form["author"]
        quote = request.form["quote"]
        db.update_quote(id, author, quote)
        return redirect("/")
    
    quote = db.select_quote(id)[0]
    return render_template("edit.html", id=id, author=quote[1], quote=quote[2])


