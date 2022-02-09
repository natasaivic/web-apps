from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import session, flash

import db

app = Flask(__name__)

# setup template reload (no caching)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    # find some top rated books
    # find some randomly picked books
    # mix it up and render on the home page
    top_books = db.get_top_books(3)
    rand_books = db.get_rand_books(3)
    return render_template("index.html", top_books=top_books, rand_books=rand_books)


@app.route("/book/<string:book_id>")
def book(book_id):
    # show the page about the book
    # show the recommendations
    book = db.get_book_info(book_id)
    similar_books = db.get_similar_books(book_id, 6)
    return render_template("book.html", book=book, similar_books=similar_books)
