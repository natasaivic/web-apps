from flask import Flask
from flask import url_for

import random
import datetime

app = Flask(__name__)

def random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

@app.route("/")
def index(): 
    return f"<center> <h1>Hello, World!</h1> <h5>Today is {datetime.datetime.today().strftime('%A')}</h5> <a href='{url_for('dice')}'>Play Dice</a> </center>"

@app.route("/dice")
def dice():
    dice = random.randint(1, 6)
    return f"<body bgcolor='{random_color()}'> <center> <h3>The dice rolled, you've got</h3> <h1>{dice}</h1><a href='{url_for('dice')}'>Roll again</a><br><br><br><br><br><a href='{url_for('index')}'>Back to index</a></center></body>" 
