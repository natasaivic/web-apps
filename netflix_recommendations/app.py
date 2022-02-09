from flask import Flask
from flask import render_template

import db

app = Flask(__name__)

# setup template reload (no caching)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    # find some newest shows
    # find some randomly picked shows
    # mix it up and render on the home page
    newest_shows = db.get_newest_shows(3)
    rand_shows = db.get_rand_shows(3)
    return render_template("index.html", newest_shows=newest_shows, rand_shows=rand_shows)


@app.route("/show/<string:id>")
def show(id):
    # show the page about the movie/tv_show
    # show the recommendations
    show = db.get_show_data(id)
    similar_shows = db.get_similar_shows(id, 6)
    return render_template("show.html", show=show, similar_shows=similar_shows)
