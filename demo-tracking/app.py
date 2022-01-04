from datetime import datetime
from flask import Flask
from flask import render_template, request, redirect, abort
from flask import session

import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = b'asdasd893asdas15hisr'


@app.route("/")
def index():
    if 'counter' not in session:
        session['counter'] = 0

    return f"OK - hello there, your counter is {session['counter']}"

@app.route("/count/<int:amount>")
def count(amount):
    if 'counter' not in session:
        return redirect("/")
    
    session['counter'] += amount
    return f"OK, your session counter is = {session['counter']}"
