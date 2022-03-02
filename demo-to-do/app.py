from flask import Flask
from flask import render_template, request, redirect
import db

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    data = db.get_all_tasks()
    print(data)
    return render_template("to-do.html", data=data)


@app.route("/new_task", methods=["POST"])
def new_task():
    task = request.form["task"]
    done = 0

    sucessful = db.save_new_task(task, done)
    if sucessful == True:
        return {"status": "OK"}
    else:
        return {"status": "ERROR"}

@app.route("/delete")
def delete():
    pass

@app.route("/done")
def done():
    pass

