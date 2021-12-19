from flask import Flask
from flask import render_template
from flask import request
import csv

from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    reminders = []
    with open('files/reminder.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            reminders.append(row)
    return render_template('index.html', items = reminders)

@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        reminder = request.form['reminder']

        with open('files/reminder.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, reminder])
        
        return redirect('/')
         
    return render_template('add.html')
