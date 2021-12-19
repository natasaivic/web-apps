import csv
from datetime import datetime
from os import write

from flask import Flask
from flask import render_template
from flask import request

from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    reminders = []
    expired = {}
    today = datetime.today().date()
    with open('files/reminder.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            reminders.append(row)
            item_date = datetime.strptime(row[0], "%Y-%m-%d").date()
            if today > item_date:
                expired[row[0]] = True

    return render_template('index.html', items=reminders, expired_dates=expired)

@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        reminder = request.form['reminder']

        with open('files/reminder.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, reminder, 0])
        
        return redirect('/')
         
    return render_template('add.html')

@app.route("/delete/<int:item_index>")
def delete(item_index):
    # load the contents of the csv file first
    reminders = []
    with open('files/reminder.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            reminders.append(row)

    # remove the nth row
    reminders.pop(item_index)

    # save the file again from the reminders list
    with open('files/reminder.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in reminders:
            writer.writerow(row)
    
    return redirect("/")

@app.route("/done/<int:item_index>")
def done(item_index):
    results = []
    with open('files/reminder.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)
    
    results[item_index][2] = 1

    with open('files/reminder.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in results:
            writer.writerow(row)

    return redirect("/")

@app.route("/undone/<int:item_index>")
def undone(item_index):
    results = []
    with open('files/reminder.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(row)

    results[item_index][2] = 0
    with open('files/reminder.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in results:
            writer.writerow(row)

    return redirect("/")
