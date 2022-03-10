from flask import Flask
from flask import render_template

import db

app = Flask(__name__)
app.config["TEMPLATES_AITO_RELOAD"] = True

@app.route("/")
def index():
    best_rated_hotels = db.get_best_rated_hotels(3)
    print(best_rated_hotels)
    random_hotels = db.get_random_hotels(3)
    print(random_hotels)
    return render_template("index.html", best_rated_hotels=best_rated_hotels, random_hotels=random_hotels)


@app.route("/hotel")
def hotel():
    return render_template("hotel.html")