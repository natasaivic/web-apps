from os import write
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
