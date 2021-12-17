import random
from datetime import datetime
from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)

def roll_dice():
    return random.randint(1, 6)

def wall_calendar():
    return datetime.now().strftime('%A %B %d. %Y ')

def wall_clock():
    return datetime.now().strftime('%H:%M')

def random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

@app.route("/")
def index(): 
    return render_template("index.html") 

@app.route("/dice")
def dice(): 
    return render_template("dice.html", dice_=roll_dice())

@app.route("/datetime")
def date_and_time():
    return render_template("datetime.html", date=wall_calendar(), time=wall_clock())

@app.route('/about')
def about(): 
    return render_template("about.html")
   