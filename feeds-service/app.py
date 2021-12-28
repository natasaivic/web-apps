from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import abort

import db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    """If user comes to the "/" index page, just redirect them to the feed page."""
    return redirect("/feed")


@app.route("/feed")
def feed():
    orderParam = request.args.get("order", "newer")
    if orderParam == "older":
        order = "ASC"
    elif orderParam == "newer" or orderParam == "":
        order = "DESC"
    else:
        return abort(400)

    pageParam = request.args.get("page", 1)
    page = int(pageParam)
    if page < 1:
        page = 1

    feed_items = db.get_feed_items(order, page)
    num_pages = db.get_number_of_pages()

    return render_template("feed.html", feed_items=feed_items, orderParam=orderParam, page=page, num_pages=num_pages)
