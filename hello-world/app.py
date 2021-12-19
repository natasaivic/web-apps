import random
from datetime import datetime
import csv

from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import redirect

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

def read_seattle_weather():
    results = []
    with open('files/seattle-weather.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  
        for row in reader:
            item = (row[0], row[2], row[5])
            results.append(item)
    return results  

def read_sportizmo():
    results = []
    with open('files/sportizmo.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # skip the headers
        for row in reader:
            item = (row[0], row[1], row[2])
            results.append(item)
    return results

@app.route("/")
def index(): 
    return render_template("index.html") 

@app.route("/dice")
def dice(): 
    return render_template("dice.html", dice=roll_dice(), random_color=random_color())

@app.route("/date")
def date_and_time():
    return render_template("date.html", date=wall_calendar(), time=wall_clock())

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/sportizmo')
def sportizmo_csv():
    return render_template("sportizmo.html", items=read_sportizmo())

@app.route('/seattle-weather')
def seattle_weather_csv():
    return render_template("seattle-weather.html", items=read_seattle_weather())

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    message = None
    if request.method == 'POST':
        name = request.form["user_name"]
        email = request.form["user_email"]
  
        with open('files/subscribed.csv', 'a') as csvfile:
            writer = csv.writer(csvfile) 
            writer.writerow([name, email])

        message = "Successfully subscribed to the newsletter list! Thank you!"
    
    return render_template("subscribe.html", message=message)
