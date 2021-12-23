from flask import Flask
from flask import render_template
from flask import request, redirect

import queries
import os.path
import db
import queries

app = Flask(__name__)

@app.route("/install")
def intall():
    if os.path.isfile("reminders.db") and queries.verify_db_setup():
        return redirect("/")

    steps = []
    if not os.path.isfile("reminders.db"):
        # create db
        db.connect()
        steps.append("DB created successfully")
    
    if not queries.verify_db_setup():
        # create table
        sql = queries.create_table()
        db.execute(sql)
        steps.append("Table created successfully")
    
    return render_template("install.html", steps=steps)

@app.route("/")
def index():
    if not os.path.isfile("reminders.db"):
        return "DATABASE NOT CREATED, CREATE DB FIRST - GO TO /install"
    
    if not queries.verify_db_setup():
        return "DATABASE TABLES NOT CREATED, CREATE THE TABLES FIRST - GO TO /install"

    return render_template("index.html", reminders=queries.select_all_reminders())


@app.route("/add" , methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        message = request.form['message']
        queries.insert_reminder(date, message)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    queries.delete_reminder(id)
    return redirect("/")

@app.route("/edit/<int:id>", methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        date = request.form['date']
        message = request.form['message']
        queries.update_database(id, date, message)
        return redirect("/")

    reminder = queries.select_reminder(id)[0]
    return render_template('edit.html', id=id, date=reminder[1], message=reminder[2])
