from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import get_flashed_messages

import db

from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
def index():
    # [
    #   (1, '2021-12-20', 'Take a walk', 0), 
    #   (2, '2021-12-20', 'Bake cookies', 0)
    # ]

    # How to implement search by criteria "q"? 
    # 1. How do we know the "q" is sent, and how do we acces it?
    searchword = request.args.get('searchword', '')
    # 2. This won't be db.get_reminders() anymore but 
    #    it should be something like db.get_by_criteria(), how do we implement it using SQL query?
    if searchword == '':
        reminders=db.get_reminders()
    else:
        reminders=db.get_by_searchword(searchword)

    return render_template('index.html', reminders=reminders, searchword=searchword)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        message = request.form['message']
        db.add_reminder(date, message)
        
        return redirect('/')

    return render_template('add.html')


@app.route("/delete/<int:reminder_id>")
def delete(reminder_id):
    db.delete_reminder(reminder_id)
    return redirect("/")


@app.route("/edit/<int:reminder_id>", methods=['POST', 'GET'])
def edit(reminder_id):
    if request.method == 'POST':
        date = request.form['date']
        message = request.form['message']
        db.edit_reminder_2(reminder_id, date, message)
        
        return redirect('/')
    
    reminder = db.edit_reminder(reminder_id)[0]
    return render_template('edit.html', reminder_id=reminder_id, date=reminder[0], message=reminder[1])
